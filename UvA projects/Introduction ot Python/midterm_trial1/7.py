"""
Question 7
Write a function called main that accepts two integers as arguments. You can assume that both are positive and the second one is larger than the first one.
Your function should return the lowest square number between the two arguments (including the arguments themselves). If there are no square numbers in the specified input range, then your function should return the Python null value None.
(A square number is a nonnegative integer, like 25, that equals the square of another integer.)
Suggestion:
You may want to use the sqrt() function in the math module to take the square root of a number. If you do, don't forget to import the math module first.
For example
If we are calling your function as:
main(19, 83)
then it should return the integer:
25
"""

def main(num1,num2):
    num0 = 0
    while num0**2 < num1:
        num0 += 1
    if num0**2 > num2:
        return None
    else:
        return num0**2 
print(main(26, 100))





