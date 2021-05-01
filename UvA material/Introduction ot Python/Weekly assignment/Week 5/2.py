"""
Write a function called 'main' that accepts a list of strings as an input.

Your function should return a list with all the strings in the input list that 
have the character 'b' in the 5th position of the string.
Remove this character from the strings in the output list. 

For example:
If we are calling your function as:
main(['cdcabaacbabb', 'cacabccdad', 'dccbaabbda', 'addbccacdbcc', 'ccaabcbdabdd', 'cadbccbdbc', 'abdbcbacac', 'bdcbbbdba', 'caadddacdcb', 'abcbdcca']) 
then it should return the list: 
['cdcaaacbabb', 'cacaccdad', 'ccaacbdabdd', 'bdcbbdba']
"""

def main(lst):
    new_lst = []
    for i in lst:
        if i[4] == 'b':
            new_lst.append(i[:4] + i[5:])
    return new_lst

#main(['cdcabaacbabb', 'cacabccdad', 'dccbaabbda', 'addbccacdbcc', 'ccaabcbdabdd', 'cadbccbdbc', 'abdbcbacac', 'bdcbbbdba', 'caadddacdcb', 'abcbdcca']) 
# test= '123456789'
# print(test[:4])
# print(test[5:])
