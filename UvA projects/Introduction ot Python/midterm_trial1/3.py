"""
Question 3
Write a function called main that accepts a string argument. The argument is the color code of an emergency warning system.
Your function should return one of the following actions depending on the color:
- "Stay inside" (for the color "red")
- "Be extra careful" (for the color "orange")
- "Be careful" (for the color "yellow")
- "Do whatever you want" (for any other color)
For example
If we are calling your function as:
main('orange')
then it should return the string:
'Be extra careful'

"""

def main(x):
    if x == 'red':
        return "Stay inside"
    elif x == 'orange':
        return "Be extra careful"
    elif x == 'yellow':
        return "Be careful" 
    else:
        return "Do whatever you want" 



