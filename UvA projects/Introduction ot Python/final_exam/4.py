"""
                                   Question 4                                   

--------------------------------------------------------------------------------

Write a function called 'main' that takes two arguments: 
(1) a list of values that can be integers ('int'), floats ('float'), strings 
('str'), or booleans ('bool'),
(2) an optional keyword argument called 'included_type' that has a default 
value of 'bool' as a Python data type

Your function should return another list that has all the elements of the input 
list (in the same order), provided that the type of the element 
equals the type stored in 'included_type'.

Hints:
1. An optional keyword argument doesn't have to be specified during a function 
   call, but that doesn't mean that it is never specified. Thus, the argument's 
   value as the function is executed may sometimes be different from its 
   default value.

For example: 
If we call your function as: 
main(['False', 2, True, False, 3.0, 'b', True])
then your function should return the list: 
[True, False, True]
"""


# 1st trial
# lst = ['False', 2, True, False, 3.0, 'b', True]
# lst2= []

# for i in lst:
#     if type(i) == bool:
#         lst2.append(i)
# print(lst2)

def main(lst, included_type=bool ):
    lst2= []
    for i in lst:
        if type(i) == included_type:
            lst2.append(i)
    return lst2
