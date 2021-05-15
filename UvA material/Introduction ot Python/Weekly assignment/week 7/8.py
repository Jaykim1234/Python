"""
Write a class called 'Main', which accepts a list of index numbers as an 
argument during object construction.

When an object is created from this class, the object should have an
attribute called 'occupied_spaces'. This attribute is a list containing
12 elements. 

The elements of the 'occupied_spaces' list should be either None (if the index
of the element is not in the input argument list) or 'c' (if it is).

For example:
If we create an object from your class as:
my_object = Main([0, 1, 3, 5])
then my_object.occupied_spaces should be equal to the list: 
['c', 'c', None, 'c', None, 'c', None, None, None, None, None, None]
"""

# lst = [0, 1, 3, 5]
# answer_lst = [None, None, None, None, None, None, None, None, None, None, None, None]

# for i in lst:
#     answer_lst[i] = 'c'
# print(answer_lst)
# lst = (1,2,4).occupied_spaces

# def Main(lst_1):
#     answer_lst = [None, None, None, None, None, None, None, None, None, None, None, None]

#     for i in lst_1:
#         answer_lst[i] = 'c'
#     return answer_lst

class Main:
    def __init__(self,list_1):
        self.occupied_spaces = ['c' if index in list_1 else None for index in range(12)]
Main(*([0, 2, 5, 7],)).occupied_spaces