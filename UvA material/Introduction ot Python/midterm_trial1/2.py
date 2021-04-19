"""
Question 2
Assume that you already have a variable called x that contains a list of strings.
Write a program that creates another list called y. Each element of y should be an integer equal to the length of the corresponding element in x.
For example
If x equals ['Amy', 'Brad', 'Cecil', '', 'Elmer']
then the value of y at the end of your program should be:
[3, 4, 5, 0, 5]
"""
#x = ['Amy', 'Brad', 'Cecil', '', 'Elmer']

lst = []
for i in x:
    lst.append(len(i))

print(lst)
