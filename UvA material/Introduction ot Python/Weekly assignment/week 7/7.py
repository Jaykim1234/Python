"""
Write a function called 'main' that accepts a string consisting of lowercase 
letters as an argument.

Your function should return a list that describes how often the letters in the
list: ['d', 'a', 'b'] occur in the input string. 

If a letter occurs only once, the description should be: 
"The string contains the character 'X' 1 time."
where X should be replaced by the letter in question.

If a letter occurs more than once, or not at all, the description should be: 
"The string contains the character 'X' N times."
where X should be replaced by the letter in question, and N by the number of
occurrences of the letter.

For example:
If we are calling your function as:
main('ebfhegggfgfhbhegfhgfa') 
then it should return the list: 
['The string contains the character 'd' 0 times.',
 'The string contains the character 'a' 1 time.',
 'The string contains the character 'b' 2 times.']
"""
# 'ebfhegggfgfhbhegfhgfa'.count('d')

# lst = ['d', 'a', 'b']

# # def main(string) :
# string = 'ebfhegggfgfhbhegfhgfa'

# result_d = 'The string contains the character ' +'"d "'+ str(string.count('d'))+ ' times.'
# result_a = 'The string contains the character ' +'"a "'+ str(string.count('a'))+ ' times.'
# result_b = 'The string contains the character ' +'"b "'+ str(string.count('b'))+ ' times.'

# print([result_d,result_a,result_b])

        
def main(string):
    count_result = [string.count('d'), string.count('a'), string.count('b')]
    print(count_result)
    print(type(string.count('d')))

    result_d = "The string contains the character 'd' "+ str(string.count('d'))
    result_a = "The string contains the character 'a' "+ str(string.count('a'))
    result_b = "The string contains the character 'b' "+ str(string.count('b'))
    
    string_result = [result_d, result_a, result_b ]
    

    for index, each_count in enumerate(count_result):
        print(string_result[index])
 
        if each_count == 1:
            string_result[index] += " time."
        else:
            string_result[index] += " times."

    return string_result

main('ebfhegggfgfhbhegfhgfa')

# new_var = print(type('ebfhegggfgfhbhegfhgfa'.count('d')))
# new_var