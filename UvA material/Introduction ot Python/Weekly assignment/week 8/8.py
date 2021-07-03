"""
Write a function called 'main' that accepts a pandas DataFrame as an input
argument.

Each row of the input DataFrame contains personal data about people under
the following column names: 'Age', 'Gender', 'Height', and 'Nationality'.

Calculate the median age in the dataset by nationality.

The result that your function returns should be a pandas Series object. Its
index should contain the possible values that nationality takes in the
dataset, and it should be sorted alphabetically. The corresponding values in
the Series should show the group medians.

You can assume that the pandas package is already imported as:
import pandas as pd

Hints:
1. DataFrames have a 'groupby' method for exactly these kind of data operations.
2. After specifying the grouping variable, select the variable to be analyzed.
3. The 'median' function calculates medians.
4. Pandas Series have a 'sort_index' method, although you may not actually
   need it if you use 'groupby', because the latter returns sorted groups
   already.


For example:
If we are calling your function as:
main(df)
where 'df' is the DataFrame:
   Age  Gender  Height Nationality
0   29  Female     165     British
1   60    Male     165      French
2   60    Male     168     British
3   61    Male     167     British
4   38      NA     177     British
5   26      NA     178      French
6   37  Female     175     British
7   41      NA     176     British

then your function should return the Series:
British    39.5
French     43.0
dtype: float64

"""

def main(df):

    return df.groupby('Nationality').median()['Age']
    