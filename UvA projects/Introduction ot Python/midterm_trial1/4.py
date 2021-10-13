"""
Question 4
Assume that you already have a variable called x that is a dictionary. Its keys are strings and its values are integers.
Check whether the string "sum of values" is among the keys of x. If it isn't, then add it as a key to x with a corresponding value that equals the sum of the original values of x.
If, on the other hand, the string "sum of values" is already among the keys of x, then don't do anything to x. Even if the corresponding value is not what it should be.
For example
If x equals {'a': 1, 'b': 2} before your program starts,
then at the end of your program, the value of x should be:
{'a': 1, 'b': 2, 'sum of values': 3}
"""
#x = {'a': 1, 'b': 8}
num = 0
while True:
    if 'sum of values' in set(x.keys()):
        break
    else:
        num = sum(x.values())
        x['sum of values'] = num
        break
print(x)






