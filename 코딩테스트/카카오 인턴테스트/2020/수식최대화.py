# https://programmers.co.kr/learn/courses/30/lessons/67257
"""
expression	            result
"100-200*300-500+20"	60420
"50*6-3*2"              300
"""

from itertools import permutations 
arr = ['*','+','-']
print(list(permutations(arr, 3)))

#[('*', '+', '-'), ('*', '-', '+'), 
# ('+', '*', '-'), ('+', '-', '*'), ('-', '*', '+'), ('-', '+', '*')]

string = "100-200*300-500+20"
order  = ('*', '+', '-')

lst_1 = []
lst_2 = []
lst_3 = []

for index in range(len(string)):
    if  string[index]  == order[0]:
        lst_1.append(index)
    elif string[index] == order[1]:
        lst_2.append(index)
    elif string[index] == order[2]:
        lst_3.append(index)
    else:
        pass

print(lst_1)
print(lst_2) 
print(lst_3)

string  = "100-200*300-500+20"
string1 =  string.split("*") 

string2 = string1.split("+") 
string2.split("-") 
string2

string3