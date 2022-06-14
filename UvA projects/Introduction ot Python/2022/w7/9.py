"""
Write a function called 'main' that accepts a string representing a date 
as "MM$DD$YYYY".

Your function should return a list with 9 string dates in that same format.

The first element of the list should be the original input date. Each further
element should be a string representing a date that is 13 days later 
than the preceding element of the list.

For example:
If we are calling your function as:
main('11$10$2016') 
then it should return the list: 
['11$10$2016', '11$23$2016', '12$06$2016', '12$19$2016', '01$01$2017', '01$14$2017', '01$27$2017', '02$09$2017', '02$22$2017']
"""

# Hint 1: You'll definitely need the datetime and timedelta classes from the 
# datetime module for this exercise. Don't forget to import them at the 
# beginning.

# Hint 2: Interpret the input string as a datetime object using the 'strptime' 
# method of the datetime class.

# Hint 3: Once you have the initial date as a datetime object, create the list
# of 9 dates by adding a sufficient number of days to the original date each 
# time. Try to do this with a list comprehension and the application of the 
# 'range' function inside it.

# Hint 4: Turn the list of 9 dates back into a list of 9 strings representing 
# dates in the appropriate format, again with a list comprehension. Use the 
# 'strftime' method of the datetime objects for creating date strings.

# Hint 5: If you feel up to it, try to combine the two list comprehensions above 
# into a single list comprehension.
from datetime import datetime
from datetime import timedelta

def main(x):
    y = []
    dt = datetime.strptime(x, '%m$%d$%Y')
    z = timedelta(days=13)
  
    y.append(dt.strftime('%m$%d$%Y'))

    for i in range(0, 8):
            dt += z  
            y.append(dt.strftime('%m$%d$%Y'))

    return y
main('11$10$2016') 