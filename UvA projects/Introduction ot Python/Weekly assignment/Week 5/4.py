"""
Write a function called 'main' that accepts one dictionary consisting of keys 
and values that are both strings with lower-case letters.

Your function should return a dictionary that is the same as the input except 
for the following cases: 
- the key does start with a vowel, or
- the value does not end with a vowel. 
Vowels include: a, e, i, o, and u.
In the above mentioned cases, the key-value pairs of the input dictionary 
should not be included in the output dictionary.

For example:
If we are calling your function as:
main({'bi': 'ueibc', 'cgf': 'oae', 'ubci': 'dc', 'iecgb': 'eibfd', 'ubf': 'agc', 
      'dbc': 'gdebc', 'eob': 'fego', 'odug': 'oe', 'ebcau': 'io', 
      'iuafo': 'aeb', 'iduag': 'ue', 'bc': 'fibd', 'du': 'efgdu', 'co': 'fio'}) 
then it should return the dictionary: 
{'cgf': 'oae', 'du': 'efgdu', 'co': 'fio'}
"""

def main(diction):
    dic_new = {}
    for index, value in diction.items():
        if (not index.startswith(('a', 'e', 'i', 'o','u'))) and (value.endswith(('a', 'e', 'i', 'o','u'))):
            dic_new[index] = value
    return dic_new

    
# #print(main({'bi': 'ueibc', 'cgf': 'oae', 'ubci': 'dc', 'iecgb': 'eibfd', 'ubf': 'agc', 
#       'dbc': 'gdebc', 'eob': 'fego', 'odug': 'oe', 'ebcau': 'io', 
#       'iuafo': 'aeb', 'iduag': 'ue', 'bc': 'fibd', 'du': 'efgdu', 'co': 'fio'}))

