"""
Write a function called 'main' that accepts a string as an argument. This 
string represents a date as DD*MM*YYYY. 

Your function should add 740 days to the input date, and return True 
if the new date is in a leap year, and False if it isn't.

A year that is divisible by 4 is a leap year, unless it is divisible by 100 but
not divisible by 400. E.g. 1996, 2000, and 2096 are leap years, but 2100 is not.

For example:
If we are calling your function as:
main('07*07*1841') 
then it should return the boolean value: 
False
"""
import datetime

# 2nd
def main(str):
    given_date = datetime.datetime.strptime('07*07*1841','%d*%m*%Y')
    plus_date = given_date + datetime.timedelta(days=740)
    if plus_date.year%4 ==0:
        if plus_date.year%100 == 0 and plus_date.year%400 != 0:
            return False
        else:
            return True
    return False




# 1st way
# def main(date):

#     import datetime

#     timeStr = date

#     Thistime = datetime.datetime.strptime(timeStr, '%d*%m*%Y')

#     now_after_740 = Thistime+ datetime.timedelta(days=740)
    
#     if (now_after_740.year%100 == 0) and (now_after_740.year%400 != 0):
#         return False

#     if now_after_740.year%4 == 0:
#         return True
#     else: 
#         return False


