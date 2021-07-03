"""
Write a function called 'main' that accepts a string as an argument.

Your function should return a string that contains only those characters from 
the original input string whose index is divisible by 3.

Note: try to solve the exercise by using string slicing only.

For example:
If we are calling your function as:
main('CkCkeYRGRrtswcvmvMqaNmsAVjrn') 
then it should return the string: 
'CkRrwmqmVn'
"""
# 2nd
def main(string):
    return string[::3]

# 1st
# def main(str_ex):
#     empty_str = ''

#     index     = 0
#     while index < len(str_ex):
#         empty_str += str_ex[index]
#         index += 3
#     return empty_str

