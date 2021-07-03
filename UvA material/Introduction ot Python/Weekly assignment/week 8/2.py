"""
Write a function called 'main' that accepts a pandas DataFrame as an input
argument.

The column names of the DataFrame are single letters, some of them lowercase,
some of them uppercase.

Your function should return another DataFrame that contains only the lowercase
columns of the original input without changing their order.

The DataFrame's index should stay the same regardless of the number of lowercase
columns.

You can assume that the pandas package is already imported as:
import pandas as pd

Hints:
1. DataFrames have a 'columns' property.
2. There is a string method for checking whether a string contains only
   lowercase letters. It is called 'islower'. But you can check whether
   a string equals its lowercase version directly just as well.
3. Don't forget how useful list comprehensions can be to construct a list from
   an iterable object.

For example:
If we are calling your function as:
main(df)
where 'df' is the DataFrame:
   A  b
0  2  6
1  7  4

then your function should return the DataFrame:
   b
0  6
1  4

"""
# 2nd

def main(df):
       list(df.columns)
       lst = [i for i in list(df.columns) if i.islower()== True]
       df = df[lst]
       return df




# 1st trial
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     'col1': ['A', 'A', 'B', 'D','E', 'C'],
#     'B': [2, 1, 9, 8, 7, 4],
#     'C': [0, 1, 9, 4, 2, 3],
#     'col4': ['a', 'B', 'c', 'D', 'e', 'F']
# })

# for column in df.columns.tolist():
#        if column.islower() == False:
#               del df[column]
              
# df
