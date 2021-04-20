"""
Question 6
Write a function called main that accepts a dictionary. The keys are integers and the values are strings.
Your function should return a dictionary that is similar to the input dictionary, but abbreviates all the values that are longer than 5 characters to their first 5 characters.
For example
If we are calling your function as:
main({1: 'some', 2: 'extralong', 3: 'words'})
then it should return the dictionary:
{1: 'some', 2: 'extra', 3: 'words'}
"""

#dict를 변수명으로 하니까 오류가 난다!!


#dict = {1: 'some', 2: 'extralong', 3: 'words'}
# for i in dict:
#     if len(dict[i]) >= 5:
#         dict[i] = dict[i][0:5]
#     else:
#         pass
# print(dict)


# items는 까먹었었는데 다시 기억하자!!
def main(diction):
    for i,v in diction.items():

        if len(diction[i]) >= 5:
            diction[i] = diction[i][0:5]
        else:
            pass
    return diction

# dict를 update하는 방법도 있다!!
