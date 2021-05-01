"""
Write a function called 'main' that accepts a list of strings.

Your function should return a list with all the strings that are longer 
than 3, but shorter than or equal to 6 characters.
Keep the original ordering.

For example:
If we are calling your function as:
main(['ERm', 'QpHgDi', 'zHQEst', 'u', 'k', 'IvYE']) 
then it should return the list: 
['QpHgDi', 'zHQEst', 'IvYE']
"""

def main(lst):
    new_lst = []
    for i in lst:
        if len(i) in range(4,7):
            new_lst.append(i)
    return new_lst
