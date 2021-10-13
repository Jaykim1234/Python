"""
Question 8
Write a function called main that accepts two strings as arguments. Both strings only consist of upper-case letters.
Your function should return a sorted list of those letters that are present in the first string, but missing from the second.
For example
If we are calling your function as:
main('MONTHY', 'PYTHON')
then it should return the list:
['M']
"""

def main(str1,str2):
    answer = ''
    for i in str1:
        if i not in str2:
            answer += i
    return sorted(answer)

main('MONTHY', 'PYTHON')

