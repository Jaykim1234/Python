"""
Question 5
Write a function called main that accepts a list as an argument.
It should return the string "long list" if the list has at least 5 elements, and the string "short list" otherwise.
For example
If we are calling your function as:
main([2, 89, 69, 57, 48])
then it should return the string:
'long list'
"""
#lst = [2, 89, 69, 57]
def main(lst):
    if len(lst)>=5:
        return 'long list'
    else:
        return 'short list'

#print(main(lst))


