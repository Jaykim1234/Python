"""
                                   Question 8                                   

No correct submissions found. Showing test results for the latest submission
--------------------------------------------------------------------------------

Write a function called 'main' that accepts a list of strings representing 
dates as "MM!DD!YYYY".

Your function should return another list that contains only those dates from 
the original input which differ by exactly 5 days from the next 
date in the input list. 

The input list is sorted from earlier to later dates and so should the output 
list be returned.

Don't forget to import the object(s) you need from the 'datetime' module.

Hints:
1. One way to convert strings representing dates to datetime objects is by 
   using the 'strptime' function of the datetime class. You can convert 
   datetimes back to strings using their 'strftime' method. 
2. To compare elements within the same list, consider iterating over the list's 
   index.
3. A datetime object minus another datetime object is a timedelta object, 
   which has an attribute you'll find useful here.

For example:
If we are calling your function as:
main(['08!21!2025', '08!28!2025', '09!02!2025', '09!07!2025', '09!09!2025', '09!14!2025', '09!19!2025', '09!27!2025', '10!03!2025', '10!08!2025', '10!14!2025', '10!22!2025', '10!23!2025', '10!28!2025']) 
then it should return the list: 
['08!28!2025', '09!02!2025', '09!09!2025', '09!14!2025', '10!03!2025', '10!23!2025']
"""
import datetime

def main(lst):
      emp_lst = []
      for index in range(len(lst)-1):
              day1 = datetime.datetime.strptime(lst[index],   "%m!%d!%Y")
              day2 = datetime.datetime.strptime(lst[index+1], "%m!%d!%Y")
              day_diff = day2- day1
              if day_diff.days == 5:
                     emp_lst.append(lst[index])
      return emp_lst
                     

# def main(tmp_lst):
#     import datetime
#     lst2 = []
#     for index in range(0, len(tmp_lst)-1):
#         day1  = datetime.datetime.strptime(tmp_lst[index],   '%m!%d!%Y')
#         day2  = datetime.datetime.strptime(tmp_lst[index+1], '%m!%d!%Y')
#         day_dif = day2- day1
#         if str(day_dif) == '5 days, 0:00:00':
#             lst2.append(tmp_lst[index])
#     return lst2
