# lst = ['cbafaed', 'fghbae', 'hgadc', 'fgcceh', 'facac', 'efafhf']
# lst2 = []
# for string in lst:
#     emp_str = ''
#     for letter in string:
#         if letter == 'd':
#             emp_str += '4'
#         elif letter == 'a':
#             emp_str += '1'
#         elif letter == 'b':
#             emp_str += '2'
#         else:
#             emp_str += letter
#     lst2.append(emp_str)
# print(lst2)

def main(lst):
    lst2 = []
    for string in lst:
        emp_str = ''
        for letter in string:
            if letter == 'd':
                emp_str += '4'
            elif letter == 'a':
                emp_str += '1'
            elif letter == 'b':
                emp_str += '2'
            else:
                emp_str += letter
        lst2.append(emp_str)
    return lst2



