"""
                                   Question 7                                   

Write a function called 'main' that accepts a pandas Series as an input 
argument. The Series contains first names. Some are spelled correctly, some are
completely in uppercase, and some are completely in lowercase.

Your function should return another Series that only contains those elements
of the input Series that end with a vowel.

The spelling of the names should be corrected to start with a capital letter
and otherwise only contain lowercase letters.

Do not alter the original order of the elements.

You can assume that the pandas package is already imported as:
import pandas as pd

Hints: 
1. Pandas Series have string methods that operate on the Series item-by-item.
   You can even do string indexing with them.
2. Pandas Series also have an 'isin' method that is excellent for checking 
   whether a Series item is contained in a collection or not.
3. You can do boolean indexing on a Series.
4. Strings have a 'capitalize' method that you can also use as a Series string 
   method to set name spellings into a proper case.


For example:
If we are calling your function as:
main(df)
where 'df' is the Series:
0     anne
1      BOB
2    cecil
3     Dave
dtype: object

then your function should return the Series:
0    Anne
3    Dave
dtype: object

"""



# 1st way
# def main(df):
    
#    index_lst =  [index for index in range(len(df.values)) if df.values[index][-1].lower() in 'aeiou']
#    df.iloc[index_lst] = df.iloc[index_lst].str.capitalize()

#    return df.iloc[index_lst]