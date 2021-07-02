"""
Write a function called 'main' that accepts a pandas DataFrame as an input
argument.

The index of the DataFrame is a pandas DatetimeIndex, but the dates are totally
unordered.

Your function should return another DataFrame that only contains those rows of
the original input for which the date in the index is in July.

Before returning the output DataFrame, put its rows in increasing chronological
order.

You can assume that the pandas package is already imported as:
import pandas as pd

Hints:
1. DataFrames have an (iterable) 'index' property.
2. The elements of a pandas DatetimeIndex have similar attributes to Python
   datetimes. For example: 'year', 'month', 'day', etc.
3. You can use the 'loc' DataFrame method to select certain rows using a list
   of indices.
4. DataFrames also have a 'sort_index' method.
5. Don't forget how useful list comprehensions can be to construct a list from
   an iterable object.


For example:
If we are calling your function as:
main(df)
where 'df' is the DataFrame:
            A  B
2021-06-16  5  9
2021-07-30  3  2
2021-05-26  2  2
2021-06-11  6  6
2021-05-01  9  5
2021-04-25  5  2
2021-04-14  3  9
2021-07-18  6  6

then your function should return the DataFrame:
            A  B
2021-07-18  6  6
2021-07-30  3  2

"""
# 2nd
def main(df):
      # df = df.loc['2021-07-01':'2021-08-01', :]
      df = df[df.index.month == 7]
      return df.sort_index()



# 1st
# def main(df):
#     z = df.loc[df.index.month == 7]
#     y = z.sort_index()
#     return y

# import pandas as pd

# df = pd.DataFrame({
#     'col1': ['A', 'A', 'B', 'D','E', 'C'],
#     'B': [2, 1, 9, 8, 7, 4],
#     'C': [0, 1, 9, 4, 2, 3],
#     'col4': ['a', 'B', 'c', 'D', 'e', 'F']
# })

# df= df.sort_values
# df