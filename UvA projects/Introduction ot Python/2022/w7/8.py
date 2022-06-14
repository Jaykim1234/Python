"""

Write a function called 'main' that accepts two strings as arguments. Both
strings represent dates as DD*MM*YYYY.

Your function should return an integer that equals the number of days with
which the earlier of the two input dates precedes the later.

For example:
If we are calling your function as:
main('16*12*2000', '27*01*2001')
then it should return the integer:
42
"""

# Hint 1: See the hints in the previous exercise about parsing a string date
# into a datetime object.

# Hint 2: Datetime objects can be subtracted from each other. Just be aware that
# the result is not an integer, but a timedelta object.

# Hint 3: Timedelta objects do have an attribute, though, which tells you how
# many days the timedelta object represents. The value of that attribute is an
# integer, and may also be negative.

# Hint 4: The 'abs' built-in function returns the absolute value of a number.

# Hint 5: Don't forget to import what you need from the datetime module!


from datetime import datetime
from datetime import timedelta


def main(dt1,dt2):
    dt1 = datetime.strptime(dt1, '%d*%m*%Y')
    dt2 = datetime.strptime(dt2, '%d*%m*%Y')

    ans = dt2- dt1
    return abs(ans.days)
