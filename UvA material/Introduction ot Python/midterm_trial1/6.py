"""
Question 6
Write a function called main that accepts a dictionary. The keys are integers and the values are strings.
Your function should return a dictionary that is similar to the input dictionary, but abbreviates all the values that are longer than 5 characters to their first 5 characters.
For example
If we are calling your function as:
main({1: 'some', 2: 'extralong', 3: 'words'})
then it should return the dictionary:
{1: 'some', 2: 'extra', 3: 'words'}
"""

#dict = {1: 'some', 2: 'extralong', 3: 'words'}
for i in dict:
    if len(dict[i]) >= 5:
        dict[i] = dict[i][0:5]
    else:
        pass
print(dict)

