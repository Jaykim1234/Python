"""

                                   Question 5                                   

Write a function called 'main' that accepts two pandas DataFrames as input 
arguments. Let's call them 'A' and 'B'. The two inputs have the same 
column names, but different indices.

Create a new DataFrame by concatenating 'A' and 'B' vertically like this:
A
A
B

Return the new DataFrame at the end of your function.

You can assume that the pandas package is already imported as:
import pandas as pd

For example:
If we are calling your function as:
main(A, B)
where 'A' is the DataFrame:
   X  Y
0  7  1
1  6  2

and 'B' is the DataFrame:
   X  Y
2  4  6
3  9  7

then your function should return the DataFrame:
   X  Y
0  7  1
1  6  2
0  7  1
1  6  2
2  4  6
3  9  7

"""

def main(A,B):
    df = pd.concat([A,A,B])
    return df