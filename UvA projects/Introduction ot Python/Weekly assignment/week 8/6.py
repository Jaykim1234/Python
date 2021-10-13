                               """
                            Question 6                                   

Write a function called 'main' that accepts a pandas DataFrame as an input 
argument.

The input DataFrame has several columns and rows. One column is called 'A', 
another one is called 'B', and there might be others as well. The values in 
the DataFrame are all integers.

Your function should return another DataFrame that only contains those rows
of the input argument for which the value in the 'A' column is 
greater than the value in the 'B' column. 

The columns in the output should be the same as in the input.

You can assume that the pandas package is already imported as:
import pandas as pd

Hints: 
1. DataFrame columns are pandas Series objects.
2. Comparing two Series objects yields another Series with True and False 
   values, corresponding to the item-by-item comparison.
3. You can do boolean indexing on a DataFrame.

For example:
If we are calling your function as:
main(df)
where 'df' is the DataFrame:
   B  A  C
0  1  3  1
1  4  4  5
2  3  3  2
3  4  5  5
4  3  2  2

then your function should return the DataFrame:
   B  A  C
0  1  3  1
3  4  5  5

"""
def main(df):
    return df.loc[df['A']> df['B']]