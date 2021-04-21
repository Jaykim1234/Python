### x contains a list of integers. Use comprehension to compile a new dictionary, where the keys are string representations of x's elements, and the values are the squares of those elements.

x = [1, 2, 3, 4]

new_list  =  {str(num):num ** 2 for num in x}

print(new_list)

### x contains a list of integers. Use comprehension to compile a new tuple, where the elements are that of x times 2.

x = [1, 2, 3, 4, 5] 

new_list = tuple([num*2 for num in x])

print(new_list)

### x contains a list of strings. Use comprehension to compile a new list, where the elements are the length of the strings.

x = ['abc', 'def', 'a', 'b', 'c', 'hi', 'hello']

new_list = [len(i) for i in x]

print(new_list)

### x contains a list of strings. Use comprehension to compile a new list, where the elements are the length of the strings.

x = ['abc', 'def', 'a', 'b', 'c', 'hi', 'hello']

new_list = [len(i) for i in x]

print(new_list)

# Dictionary is possilbe too!!!
### Use comprehension to compile a new dictionary where the keys are strings of numbers from 1 to 10, and the values are those numbers in integers.

new_dic = {str(i):i for i in range(1,11)}

print(new_dic)
