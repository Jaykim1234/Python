"""
Write a function called 'main' that accepts two strings as arguments. Both 
strings represent dates as DD$MM$YYYY. 

Your function should return an integer that equals the number of days with 
which the earlier of the two input dates precedes the later.

For example:
If we are calling your function as:
main('04$02$2010', '26$05$2012') 
then it should return the integer: 
842
"""
# 2nd
# import datetime 

# def main(input_day1, input_day2):
#     day1 = datetime.datetime.strptime(input_day1, '%d$%m$%Y')
#     day2 = datetime.datetime.strptime(input_day2, '%d$%m$%Y') # day option only are allowed
#     day_dif = day2-day1  # Use day's' option ( I think this option is only for delta?)
#     return day_dif


# 2nd
import datetime 

def main(input_day1, input_day2):
    day1 = datetime.datetime.strptime(input_day1, '%d$%m$%Y')
    day2 = datetime.datetime.strptime(input_day2, '%d$%m$%Y')
    day_dif = day2-day1

    num = ''
    for i in str(day_dif):
        if i in '0123456789':
            num += i
        if i == ' ':
            break

    return int(num)

# # 1st
# def main(day_1, day_2):

#     import datetime

#     day1  = datetime.datetime.strptime(day_1, '%d$%m$%Y')
#     day2  = datetime.datetime.strptime(day_2, '%d$%m$%Y')

#     day_dif = day2- day1

#     return day_dif.days
