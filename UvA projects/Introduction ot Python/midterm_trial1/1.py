"""
Question 1
Assume that you already have a variable called x that contains a list of numbers. Some of them are whole numbers, others are not. The whole numbers may be represented as integers (e.g.: -5, 0, 4) or as floats (e.g.: -5.0, 0.0, 4.0). The fractions, of course, are all represented as floats.
Print out a new list that contains only the whole numbers in x in their original order, all of them transformed into integers.
(Note: there is some disagreement whether the everyday term "whole number" includes non-positive numbers or not. For the purposes of this exercise, please assume that non-positive numbers are also included in the definition.)
For example
If x equals [-10, -5.4, 14.0, 3, 8, 0.001, 0.0, 0, 100, 6.2]
then your program should print the following list of integers:
[-10, 14, 3, 8, 0, 0, 100]
"""

"""
Conditions that I have gotten

x is already defined
x can be whole number, or not
should only print whole number

"""

#x= [-10, -5.4, 14.0, 3, 8, 0.001, 0.0, 0, 100, 6.2]
lst= []
for i in x:
    if int(i) ==  float(i):
        lst.append(int(i)) 
print(lst)







