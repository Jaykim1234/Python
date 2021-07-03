"""
Write a function called 'main' that accepts two pandas DataFrames as input
arguments.

The first DataFrame (let's call it 'address') has two columns: 'Name' and
'Town'. 'Name' contains people's first names, and 'Town' contains the name of
the town where they live. There may be several people in the dataset who live
in the same town.

The second DataFrame (let's call it 'province') also has two columns: 'Town'
and 'Province'. It shows which Dutch province each town is located in. In this
DataFrame, the town names are unique. The province names may, of course, be
duplicated.

Create a new column in the 'address' DataFrame and call it 'Province', too.
For each person, this column should show the name of the province in which
they live.

If a person's town is not in the 'province' DataFrame, then the 'Province'
column of the 'address' DataFrame should contain the string '-'.

Return the extended 'address' DataFrame at the end of your function.

You can assume that the pandas package is already imported as:
import pandas as pd

Hints:
1. What you really want is a simple DataFrame left merge.
   Check out the 'merge' DataFrame method.
2. When pandas finds no match during a merge operation, it enters a missing
   value in the corresponding DataFrame cell.
3. Missing values in a DataFrame can easily be replaced. Take a look at the
   'fillna' DataFrame method.


For example:
If we are calling your function as:
main(address, province)
where 'address' is the DataFrame:
       Name     Town
0       Una  Sittard
1    Elisha   Arnhem
2  Margaret   Berlin
3    Violet   Arnhem

and 'province' is the DataFrame:
       Town    Province
0   Sittard     Limburg
1   Heerlen     Limburg
2     Venlo     Limburg
3     Zeist     Utrecht
4    Houten     Utrecht
5    Rhenen     Utrecht
6    Arnhem  Gelderland
7       Ede  Gelderland
8  Nijmegen  Gelderland

then your function should return the DataFrame:
       Name     Town    Province
0       Una  Sittard     Limburg
1    Elisha   Arnhem  Gelderland
2  Margaret   Berlin           -
3    Violet   Arnhem  Gelderland

"""

def main(A,B):
    df = pd.merge(A, B, on ='Town', how ='left' ).fillna('-')
    return df