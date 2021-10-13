"""
Write a function called 'main' that accepts a pandas DataFrame as an input 
argument.

The input DataFrame has at least 4 columns, and the column names are single 
letters. The values in the DataFrame are all integers.

Your function should return another DataFrame in which the rows are sorted 
by the values in the fourth column in decreasing order.

You can assume that the pandas package is already imported as:
import pandas as pd

Hint: DataFrames have a 'sort_values' method.

For example:
If we are calling your function as:
main(df)
where 'df' is the DataFrame:
    g   w   a   e
0  96  53  21  77
1  23  10  50  98
2  38  84  80  93

then your function should return the DataFrame:
    g   w   a   e
1  23  10  50  98
2  38  84  80  93
0  96  53  21  77

"""

# df.sort_values(by='col1', **p)

# 2nd way

def main(df):
    return df.sort_values(by=df.columns[3], ascending =False)




# 1st way
# import pandas as pd

# def main(df):

#     df= df.sort_values(by= df.columns[3] , ascending= False)

#     return df


# import pandas as pd
# df = pd.DataFrame({
#     'col1': ['A', 'A', 'B', 'D','E', 'C'],
#     'col2': [2, 1, 9, 8, 7, 4],
#     'col3': [0, 1, 9, 4, 2, 3],
#     'col4': ['a', 'B', 'c', 'D', 'e', 'F']
# })
# df
# df= df.sort_values(by= df.columns[3] , ascending=True)
# df.iloc[1:2, 3]