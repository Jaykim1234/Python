"""
Write a function called 'main' that accepts a string as an argument.

Take the first 2 characters of the string, and call this a substring
of the original input argument.

Your function should return a list with the starting indices of all occurences 
of this substring in the original input argument.

Hint: consider using the 'find' string method iteratively, starting the search 
for the substring progressively later after each successful find. 
Alternatively, you can get creative with the 'split' string method, too.

For example:
If we are calling your function as:
main('zphgkzppvsqtvdylsonezpzp') 
then it should return the list: 
[0, 5, 20, 22]
"""

# find_str = 'zphgkzppvsqtvdylsonezpzp'

# lst = []
# index = 0
# while index < len(find_str)-1:
#     spot   = find_str.find('zp', find_str.find(find_str[:2], 0) + index)
#     index += 1
#     lst.append(spot)

# print(sorted(list(set(lst))))

def main(find_str):
    lst = []
    index = 0
    while index < len(find_str)-1:
        spot   = find_str.find(find_str[:2], find_str.find(find_str[:2], 0) + index)
        index += 1
        
        if spot == -1:
            break
        lst.append(spot)

    return sorted(list(set(lst)))

main(*('kveonpizkvkvwrlbpvjxncjsuqz',))
