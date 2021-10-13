"""
Write a function called 'main' that accepts a list consisting of values of
any type.

Your function should return a tuple with all the float values multiplied by 
4. Ignore all other elements.

For example:
If we are calling your function as:
main(['j', 6, 'k', 1.59, 1, 9, 'd', True, 9, 's', 4.78, (), 'p', 11.15, 'g']) 
then it should return the tuple: 
(6.36, 19.12, 44.6)
"""
def main(lst):
    new_lst = []
    for i in lst:
        if type(i) == float:
            new_lst.append(i*4)
    return tuple(new_lst)
#print(main(['j', 6, 'k', 1.59, 1, 9, 'd', True, 9, 's', 4.78, (), 'p', 11.15, 'g']) )