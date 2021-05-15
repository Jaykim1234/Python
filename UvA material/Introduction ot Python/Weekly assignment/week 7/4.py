"""
Write a function called 'main' that accepts a string with an even number of 
characters as an argument. Lowercase letters have an even index in the string 
and uppercase letters have an odd index in the string.

Your function should return a string consisting of odd-indexed 
characters in the same order, concatenated with even-indexed
characters in the reverse order.

Note: try to solve the exercise on a single line (apart from the function 
header) using string slicing.

For example:
If we are calling your function as:
main('mUvEnHeLzKcVfNtNgXmKdTwVeEjE') 
then it should return the string: 
'UEHLKVNNXKTVEEjewdmgtfczenvm'
"""
# def main(given_str):
#     upper_str = ''
#     lower_str = ''

#     for letter in given_str:
#         if letter.isupper() == True:
#             upper_str += letter
#         else:
#             lower_str =  lower_str + letter 

#     answer = upper_str + lower_str

#     return answer

def main(given_str):
    upper_str = ''
    lower_str = ''

    for letter in given_str:
        if letter.isupper() == True:
            upper_str += letter
        else:
            lower_str += letter 

    answer = upper_str[::-1] + lower_str

    return answer

main('mUvEnHeLzKcVfNtNgXmKdTwVeEjE')


string = '123456'
string[::-1]
