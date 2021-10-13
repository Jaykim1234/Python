"""
Write a function called 'main' that accepts one list consisting of 
one-character strings.

Your function should return a list of two-character strings. 

The first characters in the output list should be the same as the characters in 
the input list at the same positions.

The second characters in the output list should be the same as the characters 
in the input list 2 positions later.
If, for the second character, you have reached the end of the input list, 
start again at the beginning.

Hint: List slicing and concatenation, list comprehensions, and the zip()
function may all come in handy for a concise solution.

For example:
If we are calling your function as:
main(['c', 'w', 'w', 'a', 'u', 'g', 'b', 'w', 'o', 'f']) 
then it should return the list: 
['cw', 'wa', 'wu', 'ag', 'ub', 'gw', 'bo', 'wf', 'oc', 'fw']
"""

# lst =  ['c', 'w', 'w', 'a', 'u', 'g', 'b', 'w', 'o', 'f']
# print(lst*2)

# long_lst = lst*2
# new_lst = []

# for i in range(len(lst)):
#     new_lst.append(long_lst[i]+ long_lst[i+2])
# return new_lst

def main(lst):
    long_lst = lst*2
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(long_lst[i]+ long_lst[i+2])
    return new_lst

