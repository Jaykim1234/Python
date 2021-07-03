"""
Write a function called 'main' that accepts a pandas DataFrame as an input 
argument.

Each row of the input DataFrame contains data about babies. The DataFrame has
a column called 'Height' that contains a baby's height in centimeters as an
integer.

Create a new column called 'Height (m)' that stores each baby's 
height in meters as a floating point number.

Return the input DataFrame with the new column at the end.

You can assume that the pandas package is already imported as:
import pandas as pd


For example:
If we are calling your function as:
main(df)
where 'df' is the DataFrame:
   Height  Weight
0      44    3540
1      52    3210
2      46    4270
3      43    3600
4      50    4130

then your function should return the DataFrame:
   Height  Weight  Height (m)
0      44    3540        0.44
1      52    3210        0.52
2      46    4270        0.46
3      43    3600        0.43
4      50    4130        0.50

"""
# 2nd 
def main(df):
       df['Height (m)'] = df['Height']/100
       return df

# 1st way
# import pandas as pd
# 
# df = pd.DataFrame({
#     'col1': ['A', 'A', 'B', 'D','E', 'C'],
#     'B': [2, 1, 9, 8, 7, 4],
#     'C': [0, 1, 9, 4, 2, 3],
#     'col4': ['a', 'B', 'c', 'D', 'e', 'F']
# })

# df['Height (m)'] = df['B']/100
# df

# def main(df):
#     df['Height (m)'] = df['Height']/100 
#     return df