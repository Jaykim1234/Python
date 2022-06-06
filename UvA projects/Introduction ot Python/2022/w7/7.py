"""
Write a function called 'main' that accepts a string as an argument. This
string represents a date as DD$MM$YYYY.

Your function should add 720 days to the input date, and return True
if the new date is in a leap year, and False if it isn't.

A year that is divisible by 4 is a leap year, unless it is divisible by 100 but
not divisible by 400. E.g. 1996, 2000, and 2096 are leap years, but 2100 is not.

For example:
If we are calling your function as:
main('21$12$1813')
then it should return the boolean value:
False

# Hint 1: You'll need to use certain parts of the datetime module. Don't forget
# to import them at the start of your code! (That is: before you even define
# the 'main' function.)

# Hint 2: Use the 'strptime' function of the datetime class to turn the input
# string into a datetime object. Just think carefully about the template
# according to which you want to parse the input string.

# Hint 3: Once you have a datetime object, add 720 days to it. To do
# that, you also need another class from the datetime module: 'timedelta'.

# Hint 4: Extract the year as an integer from the resulting datetime object,
# and write a bunch of if-statements to decide whether it is a leap year or not.
"""
from datetime import datetime
from datetime import timedelta
def main(dt):
    dt = datetime.strptime(dt, '%d$%m$%Y')
    x = timedelta(days=720)

    new_date = dt + x

    if new_date.year%4 == 0:
        if new_date.year%100 == 0 and new_date.year%400 != 0:
            return False
        else:
            return True
    else:
        return False


# def main(dt):
#     dt = datetime.strptime(dt, '%d$%m$%Y')
#     x = timedelta(days=720)

#     new_date = dt + x

#     print(new_date)
#     new_date.strftime('%d$%m$%Y')
    
#     if int(datetime.year(new_date)) % 4 == 0:
#         int(new_date) == True
#     else:
#         int(new_date) == False
    
#     return new_date

# def main(dt):
#     dt = datetime.strptime(dt, '%d$%m$%Y')
#     x = timedelta(days=720)

#     new_date = dt + x

#     print(new_date)
#     new_date.strftime('%d$%m$%Y')
    
#     if int(datetime.year(new_date)) % 4 == 0:
#         int(new_date) == True
#     else:
#         int(new_date) == False
    
#     return new_date

print(main('21$12$1813'))