import warnings
import copy
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import os 
from typing import List
from operator import add
from toolz import reduce, partial
from scipy import stats
from scipy.optimize import fmin_slsqp
from scipy.stats import ttest_ind
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,Ridge
from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import pyplot as plt


def graph_original(country, interested_variable, data0):
  """
  Make graph with interested variable and country
  This function is to visulize the raw data 
  
  The name of country column should be "country"
  The name of year column should be "year"

  """
  # Make data0set that is only about entered country 
  str_expr = f"country == '{country}' " 
  data0_new = data0.query(str_expr) 
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize='x-small')
  plt.rc('ytick', labelsize='x-small')  
  plt.figure(figsize=(10,6)) 
  plt.plot(data0_new['year'], data0_new[interested_variable], label=interested_variable,color='black', lw=1)
  plt.legend();

def agumented_synthetic_control(country, main_variable, data0, incident= 'QE', std_scaling=True, incident_year= 2009):
  """
  This function is to make dataframe that contain the value of ASCM

  Country : The country you want to see
  pool: list of country in data set
  main_variable: Variable you want to see. ex) CA
  data0 : data that you have
  
  The name of country column should be "country"
  The name of year column should be "year"
  """

  #standard scaling for control variables
  if std_scaling:
    features = [feature for feature in data0.columns if feature not in ['country', 'year', main_variable]]
    data0[features] = StandardScaler().fit_transform(data0[features])
  
  #Make new dummy variable 'QE'
  data0[incident] = [1 if t else 0 for t in list(data0['year'] > incident_year)]

  # make data only about selected country
  str_expr = f"country == '{country}' "   
  data0_country = data0.query(str_expr) 

  # .T  flip the table to have one column per state
  features = [feature for feature in data0.columns if feature not in ['country', 'year', main_variable]]
  condition = incident + " == 0"

  inverted = data0.query(condition).pivot(index='country', columns="year")[features].T
  
  # Replace the missing value
  inverted = inverted.fillna(method='pad')
  
  # Set X and y
  y = inverted[country].values
  X = inverted.drop(columns= country).values
  
  # Find the weight of countries in the pool or a given dataset
  weights_ridge = Ridge(fit_intercept=False).fit(X, y).coef_
  weights_ridge.round(3)

  #select countries without country and make tables about main variable entered
  data1 = data0.query(f"country != '{country}' ").pivot(index='year', columns="country")[main_variable]

  # multiply values of main variable with weight that we have gotten
  data_synth_lr = data1.values.dot(weights_ridge)
  data0_country['ASCM'] = data_synth_lr

  return data0_country

def rmse(y_true, y_pred):
    '''
    Compute Root Mean Square Percentage Error between two arrays.
    '''
    loss = np.sqrt(np.mean(np.square(((y_true - y_pred) / y_true)), axis=0))

    return loss

def ascm_dataframe(country, main_variable, data0, incident= 'QE', std_scaling=True, incident_year= 2009):

  # Deepcopy dataframe
  data1 = copy.deepcopy(data0)

  # Make dataframe that contain values of augmented synthetic control
  data2 = agumented_synthetic_control(country, main_variable, data0, incident= 'QE', std_scaling=True, incident_year= 2009)

  # Add column of difference
  data2['Difference'] = data2[main_variable]- data2['ASCM']

  # Make dataframe that contain pre-treatment period only
  data_pre = data2.loc[data2.year <= incident_year ]

  # Make dataframe that contain post-treatment period only
  data_post = data2.loc[data2.year > incident_year ]

  # Calculate RMSPE for pre-treatment period only
  rmspe = rmse(data_pre[main_variable], data_pre['ASCM'])
  print('Pre- RMSPE :', rmspe )

  # Calculate RMSPE for post-treatment period only
  rmspe = rmse(data_post[main_variable], data_post['ASCM'])
  print('Post- RMSPE :', rmspe )

  return data2[['country','year',main_variable,'ASCM','Difference']]


# Country : The country you want to see
# main_variable: Variable you want to see. ex) CA
# data0 : data that you have

def agumented_weight_visualize(country, main_variable, data0, incident= 'QE', incident_year=2009):
  """
  This function is for showing the weight of countries from ridge ASMC

  # Country : The country you want to see
  # main_variable: Variable you want to see. ex) CA
  # data0 : data that you have
  """

  #Make new dummy variable 'QE'
  data0[incident] = [1 if t else 0 for t in list(data0['year'] > incident_year)]

  # make data only about selected country
  str_expr = f"country == '{country}' "   
  data0_country = data0.query(str_expr) 

  # .T  flip the table to have one column per state
  features = [feature for feature in data0.columns if feature not in ['country', 'year', main_variable]]
  condition = incident + " == 0"
  inverted = data0.query(condition).pivot(index='country', columns="year")[features].T
  
  # Replace the missing value
  inverted = inverted.fillna(method='pad')
  
  # Set X and y
  y = inverted[country].values
  X = inverted.drop(columns= country).values
  
  # Find the weight of countries in the pool or a given dataset
  weights_ridge = Ridge(fit_intercept=False).fit(X, y).coef_
  weights_ridge_rounded = weights_ridge.round(3)

  # Show weight of countries in the pool
  pool = list(data0['country'].unique())

  dic = {}
  for index in range(len(pool)-1):
    dic[pool[index]] = weights_ridge_rounded[index]
  return dic





def ascm_visualize(country, main_variable, data0, incident= 'QE', incident_year=2009, std_scaling=True, ylabel=False):
  
  """
  Country : The country you want to see
  pool: list of country in data set
  main_variable: Variable you want to see. ex) CA
  data0 : data that you have
  """

  #standard scaling for control variables
  if std_scaling:
    features = [feature for feature in data0.columns if feature not in ['country', 'year', main_variable]]
    data0[features] = StandardScaler().fit_transform(data0[features])
  
  #Make new dummy variable 'QE'
  data0[incident] = [1 if t else 0 for t in list(data0['year'] > incident_year)]

  # make data only about selected country
  str_expr = f"country == '{country}' "   
  data0_country = data0.query(str_expr) 

  # .T  flip the table to have one column per state
  features = [feature for feature in data0.columns if feature not in ['country', 'year', main_variable]]
  condition = incident + " == 0"
  inverted = data0.query(condition).pivot(index='country', columns="year")[features].T
  
  # Replace the missing value
  inverted = inverted.fillna(method='pad')
  
  # Set X and y
  y = inverted[country].values
  X = inverted.drop(columns= country).values
  
  # Find the weight of countries in the pool or a given dataset/ Calculate the weight through Ridge regression.
  weights_ridge = Ridge(fit_intercept=False).fit(X, y).coef_
  
  # Show weight of countries in the pool
  pool = list(data0['country'].unique())

  #select countries without country and make tables about main variable entered
  data1 = data0.query(f"country != '{country}' ").pivot(index='year', columns="country")[main_variable]
  
  # multiply values of main variable with weight that we have gotten
  data_synth_lr = data1.values.dot(weights_ridge)

  # interest variable data with interested country only
  data_2 = data0.query(f"country == '{country}'")[main_variable]
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize='x-small')
  plt.rc('ytick', labelsize='x-small')
  plt.figure(figsize=(10,6))
  plt.plot(data0.query(f"country == '{country}'")["year"], data_2, label=f"{country}",color='dimgray', linestyle=":", lw=1)
  plt.plot(data0.query(f"country == '{country}'")["year"], data_synth_lr, label="Augmented Synthetic Control",color='black', lw=1)

  val_max = max(data_synth_lr.max(),data_2.max())
  val_min = min(data_synth_lr.min(),data_2.min())
  
  plt.grid(False)
  plt.vlines(x=incident_year , ymin= val_min, ymax=val_max , linestyle=":", lw=2, label="QE")
  
  # if there is no input for y label, the default label is the name of the main variable
  if ylabel == False:
    ylabel = main_variable

  plt.ylabel(f"{ylabel}")


def rmspe_table(country, main_variable, data0,  incident= 'QE' ,incident_year=2009, outlier = 0):
  # Deepcopy dataframe
  data1 = copy.deepcopy(data0)
  
  # Make list that contain names of countries
  pool = list(data1['country'].unique())
  
  # find the first country of this dataset 
  first_country = list(data0['country'])[0]

  # check the number of data for first country
  first_country_data_number = data0.loc[data0['country'] == first_country].shape[0]

  # make empty list to store values
  country_lst = []
  rmspe_ratio_lst = []
  country_ratio = []

  for each_country in pool:

    str_expr = f"country == '{each_country}' " 
    data0_new = data0.query(str_expr) 

    # here we will check whether the number of data for other countries would be the same
    # not all countries have the smae number of yearly data
    if first_country_data_number == data0_new.shape[0]:

      # Make dataframe that contain values of augmented synthetic control
      data2 = agumented_synthetic_control(each_country, main_variable, data1,  incident= 'QE' , std_scaling=True, incident_year=incident_year)

      # Add column of difference
      data2['Difference'] = data2[main_variable]- data2['ASCM']

      # Make dataframe that contain pre-treatment period only
      data_pre = data2.loc[data2.year <= incident_year ]

      # Make dataframe that contain post-treatment period only
      data_post = data2.loc[data2.year > incident_year ]

      # Calculate RMSPE for pre-treatment period only
      rmspe_pre = rmse(data_pre[main_variable], data_pre['ASCM'])

      # Calculate RMSPE for post-treatment period only
      rmspe_post = rmse(data_post[main_variable], data_post['ASCM'])


      # append results to lists for plotting
      country_ratio.append([each_country,rmspe_post/rmspe_pre])
      
  # sort rmspe_ratio based on values
  country_ratio.sort(key = lambda x: x[1])
  
  # delete outliers
  country_ratio2 = country_ratio[0:len(country_ratio)-outlier]


  # make a list of deleted countries
  deleted_country = []

  # append deleted country to an empty list
  if outlier !=0:
    for i in range(outlier):
      deleted_country.append(country_ratio[len(country_ratio)-1-(i+1)][0])
      
  
  country_lst = [ country for country, ratio in country_ratio2] # list that contain country name
  rmspe_ratio_lst = [ ratio for country, ratio in country_ratio2] # list that contain rmspe ratio
  country_lst_np = np.array(country_lst)
  rmspe_ratio_lst_np = np.array(rmspe_ratio_lst)
  
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize='x-small')
  plt.rc('ytick', labelsize='x-small')  
  plt.figure(figsize=(10,6)) 
  col = np.where(country_lst_np == country,'r' , np.where(country_lst_np=='p','k','black')) # set conditions of color  
  plt.scatter(country_lst_np, rmspe_ratio_lst_np, c= col , label='rmspe_post/rmspe_pre')
  plt.xticks(rotation=90)
  plt.ylabel('rmspe ratio')
  plt.legend();

def p_value(interested_country, interested_variable, data0, incident_year = 2009, detail = False):
  """
  Note
  Treatment effect = the value of interested varaible - value of Agumented synthetic control ( The subject here is the interested country)
  Placebo effect = the value of interested varaible - value of Agumented synthetic control ( The subject here is the all the other country except the main country)

  P-value is calculated with following two steps 
  - 1st step : Count the number of placebo effects that have larger absolute values than those of treatment effects.
  - 2nd step : Divide the value from 1st step by the total number of countries 
  """

  # Make list that contains sum of absolute placebo effect value
  placebo_all_year = []

  # Make list that contains sum of absolute treatment effect value
  treatment_all_year = []

  # Make a list of country in a dataset
  pool = list(data0['country'].unique())
  
  # Make list of year in a dataframe
  pool_year = list(data0['year'].unique())
  current_year = incident_year
  
  # find the first country of this dataset 
  first_country = list(data0['country'])[0]

  # check the number of data for first country
  first_country_data_number = data0.loc[data0['country'] == first_country].shape[0]

  # make empty lists for plotting
  lst_year =[]
  lst_p_value = []  

  for year in range(-9,0):# year is -13,-12,-11 ... This is to select ASCM from 2008 to 2021
    synth_list = []
    current_year += 1

    for country in pool:
      str_expr = f"country == '{country}' " 
      data0_new = data0.query(str_expr) 

      if first_country_data_number == data0_new.shape[0]:      
        # Make temporary dataframe that contains synthetic values
        temp_dataframe = agumented_synthetic_control(country, interested_variable, data0)
        
        # print(temp_dataframe)
        value_agumented_synthetic_control  = temp_dataframe.iloc[year,-1] # (left: row), (right:column)
        value_interested_variable  = temp_dataframe.iloc[year,2]

        # print(value_interested_variable, value_synthetic_control)
        placebo_effect = value_interested_variable - value_agumented_synthetic_control
        synth_list.append(placebo_effect)

    # Calculate synthetic value for interested country in 2020 year
    synth_interested_country = agumented_synthetic_control(interested_country, interested_variable, data0)

    value_agumented_synthetic_control_main_country = synth_interested_country.iloc[year,-1]
    value_interested_variable_main_country = synth_interested_country.iloc[year,2]

    treatment_effect = value_interested_variable_main_country - value_agumented_synthetic_control_main_country

    treatment_all_year.append(abs(treatment_effect))
    # Make dictionray to summarise placebo effect
    
    placebo_effect_dictionary = {}
    for now_country, placebo_value in zip(pool[0:-1],synth_list[0:-1]):
      placebo_effect_dictionary[now_country] = placebo_value
    

    # Make a new list that contains placebo effects which are larger than the treatment effect
    sorted_list= [placebo_effect for placebo_effect in synth_list if abs(placebo_effect) > abs(treatment_effect)]

    p_value = len(sorted_list)/(len(synth_list)-1) # -1: exclude the interested country in the list
    
    # if detail option is True. Here we can find the detailed values of p-values
    if detail:

      print('Placebo effects:',placebo_effect_dictionary )
      # Print treament effect
      print(f'Treatment Effect for the Year {current_year} ({interested_country}): {treatment_effect}')
      print(f'p-value : {p_value}')
      print('')
      print('')
  
    # append results to lists for plotting
    lst_year.append(current_year)
    lst_p_value.append(p_value)


  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize='x-small')
  plt.rc('ytick', labelsize='x-small')  
  plt.figure(figsize=(10,6)) 
  plt.scatter(lst_year, lst_p_value, label='p_value')
  plt.ylabel('p_value')
  plt.legend();


def placebo(interested_country, interested_variable, data0, incident_year=2009, std_scaling=True, ylabel=False):

  # standard scaling for control variables
  if std_scaling:
    features = [feature for feature in data0.columns if feature not in ['country', 'year', interested_variable]]
    data0[features] = StandardScaler().fit_transform(data0[features])

  # Make a list of country in a dataset
  pool = list(data0['country'].unique())
  
  # find the first country of this dataset 
  first_country = list(data0['country'])[0]

  # check the number of data for first country
  first_country_data_number = data0.loc[data0['country'] == first_country].shape[0]

  synth_list = []
  for country in pool:
    str_expr = f"country == '{country}' " 
    data0_new = data0.query(str_expr) 
    
    if first_country_data_number == data0_new.shape[0]:
      # Make temporary dataframe that contains synthetic values
      temp_dataframe = agumented_synthetic_control(country, interested_variable, data0)
      synth_list.append(temp_dataframe)
  
  # Make gahtered data
  data_synth_all= pd.concat(synth_list, axis = 0, sort= False)

  # Make a plot for all country except interested_country
  plt.figure(figsize=(10,6))
  plt.plot(data_synth_all['year'],data_synth_all[f'{interested_variable}']-data_synth_all['ASCM'],alpha=.6, label = 'placebo effect',color='dimgray', linestyle=":", lw=1) 
  
  # Make a plot for interested country
  temp_dataframe2 = agumented_synthetic_control(interested_country, interested_variable, data0)
  
  plt.plot(temp_dataframe2['year'],temp_dataframe2[f'{interested_variable}']-temp_dataframe2['ASCM'], alpha=.6, label = f'QE impact on {interested_country}',color='black', lw=1.5)
  plt.rc('font', family='serif')
  plt.rc('xtick', labelsize='x-small')
  plt.rc('ytick', labelsize='x-small')
  plt.grid(False)

  # if there is no input for y label, the default label is the name of the main variable
  if ylabel == False:
    ylabel = interested_variable

  plt.ylabel(f"{ylabel}")
  plt.legend();  
  plt.show()

def ascm_limit_donor_pool(country, main_variable, data0, incident= "QE", incident_year=2009, std_scaling=True, detail= False, ylabel=False):

  # standard scaling for control variables
  if std_scaling:
    features = [feature for feature in data0.columns if feature not in ['country', 'year', main_variable]]
    data0[features] = StandardScaler().fit_transform(data0[features])

    country_list  = list(data0['country'].unique())
    count = 1
    while len(country_list) > 1 :
        data0 = data0.loc[data0.country.isin(country_list) == True]
        
        if detail:
          print("")
          print(f"< List of countries after {count} exclusion >")
          print('')
          print('Countries:', country_list[0:-1])

        #Make new dummy variable 'QE'
        data0[incident] = [1 if t else 0 for t in list(data0['year'] > incident_year)]

        # make data only about selected country
        str_expr = f"country == '{country}' "   
        data0_country = data0.query(str_expr) 

        # .T  flip the table to have one column per state
        features = [feature for feature in data0.columns if feature not in ['country', 'year', main_variable]]
        condition = incident + " == 0"
        inverted = data0.query(condition).pivot(index='country', columns="year")[features].T
        
        # Replace the missing value
        inverted = inverted.fillna(method='pad')
        
        # Set X and y
        y = inverted[country].values
        X = inverted.drop(columns= country).values
        
        # Find the weight of countries in the pool or a given dataset/ Calculate the weight through Ridge regression.
        weights_ridge = Ridge(fit_intercept=False).fit(X, y).coef_

        # Show weight of countries in the pool
        pool = list(data0['country'].unique())

        
        #select countries without country and make tables about main variable entered

        data1 = data0.query(f"country != '{country}' ").pivot(index='year', columns="country")[main_variable]

        # multiply values of main variable with weight that we have gotten
        data_synth_lr = data1.values.dot(weights_ridge)
        plt.rc('font', family='serif')
        plt.rc('xtick', labelsize='x-small')
        plt.rc('ytick', labelsize='x-small')
        plt.figure(figsize=(10,6))
        plt.plot(data0.query(f"country == '{country}'")["year"], data0.query(f"country == '{country}'")[main_variable], label=f"{country}", color='dimgray', linestyle=":", lw=1, alpha=.6 )
        plt.plot(data0.query(f"country == '{country}'")["year"], data_synth_lr, label=f"ASCM exclude {count} / {country_list[0]}", color='black', lw=1)
        plt.legend();
        plt.grid(False)
          # if there is no input for y label, the default label is the name of the main variable
        if ylabel == False:
          ylabel = main_variable
        plt.ylabel(f"{ylabel}")


        country_list.pop(0)
        count += 1