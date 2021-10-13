"""
                                   Question 9                                   

--------------------------------------------------------------------------------

Write a function called 'main' that accepts a pandas DataFrame as an input 
argument.

The input DataFrame has several columns and rows. The values in the DataFrame 
are all integers.

Your function should return another DataFrame that only contains those rows
of the input argument for which the value in the rightmost column is an
odd number.

The columns in the output should be the same as in the input.

You can assume that the pandas package is already imported as:
import pandas as pd

Hints:
1. DataFrames have a 'columns' property, the output of which works like a list.
2. You can apply operations like '//', '%', or '==' to DataFrame columns, which 
   then work element-by-element to create a pandas Series.
3. You can use boolean indexing with a Series to select DataFrame rows. 

For example:
If we are calling your function as:
main(df)
where 'df' is a DataFrame with the data:
    V   X   P
0  25  22  93
1  90  56  67
2  32  19  48
3  41  45  75

then your function should return a DataFrame with the data:
    V   X   P
0  25  22  93
1  90  56  67
3  41  45  75

"""
def main(df):
    return df.loc[df[df.columns[-1]]%2 != 0]
    

# Solution 1
# def main(df):
#     df = df.loc[df.iloc[:,-1]%2 != 0]
#     return df


# 1st trial
# def main(df):
#     # for idx in range(len(df)):
#     #     row = idf.iloc[idx,:]
#     #     if row[-1]%2 == 0:
#     #         continue
#     #     df_ = df_.append
#     # for i,x in enumerate(df):

#     #      if df[df.columns[-1]] %2 == 0:
#     #          df= df.drop(labels=i)
    
#     return df

