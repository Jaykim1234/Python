"""
Write a function called 'main' that accepts one list as an argument. The list 
consists of sublists, in which the first element is a string and the other
8 elements are integers. 

Your function should return a dictionary, where the keys are the strings from 
every sublist and the values are sub-dictionaries. 

The values of the sub-dictionaries are the integers of the sublists. 
The keys of the sub-dictionaries are strings from the following list (in this 
order): ['income', 'age', 'ranking', 'score', 'weight', 'spent', 'length', 'average']

Hint: Try to solve this problem with a dictionary comprehension inside another 
dictionary comprehension. Alternatively, build the outside dictionary with a
for-loop, and the sub-dictionaries inside with a dict comprehension.

For example:
If we are calling your function as:
main([['Vidya', 58, 71, 58, 73, 67, 51, 56, 69], ['Arya', 78, 54, 50, 65, 54, 64, 65, 66], ['Anaitha', 72, 80, 53, 53, 59, 54, 77, 59]]) 
then it should return the dictionary: 
{'Vidya': {'income': 58, 'age': 71, 'ranking': 58, 'score': 73, 'weight': 67, 'spent': 51, 'length': 56, 'average': 69}, 
 'Arya': {'income': 78, 'age': 54, 'ranking': 50, 'score': 65, 'weight': 54, 'spent': 64, 'length': 65, 'average': 66}, 
 'Anaitha': {'income': 72, 'age': 80, 'ranking': 53, 'score': 53, 'weight': 59, 'spent': 54, 'length': 77, 'average': 59}}
"""

def main(lst):
    import copy
    dic_answer = {}
    dic = {'income': None, 'age': None, 'ranking':None , 'score':None, 'weight':None , 'spent': None, 'length': None, 'average':None }
    #lst = [['Vidya', 58, 71, 58, 73, 67, 51, 56, 69], ['Arya', 78, 54, 50, 65, 54, 64, 65, 66], ['Anaitha', 72, 80, 53, 53, 59, 54, 77, 59]]
    print(lst[0][0])
    for i in range(len(lst)):
        dic_new = copy.deepcopy(dic)
        dic_new['income'] = lst[i][1]
        dic_new['age'] = lst[i][2]
        dic_new['ranking'] = lst[i][3]
        dic_new['score'] = lst[i][4]
        dic_new['weight'] = lst[i][5]
        dic_new['spent'] = lst[i][6]
        dic_new['length'] = lst[i][7]
        dic_new['average'] = lst[i][8]

        dic_answer[lst[i][0]] = dic_new
    return dic_answer

    #main([['Vidya', 58, 71, 58, 73, 67, 51, 56, 69], ['Arya', 78, 54, 50, 65, 54, 64, 65, 66], ['Anaitha', 72, 80, 53, 53, 59, 54, 77, 59]])
