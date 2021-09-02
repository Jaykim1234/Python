"""
소수 찾기
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
출처
"""

from itertools import permutations
import math

def solution(numbers):
    import itertools
    
    def check(num):
        tmp_num = 0
        for i in range(1, num+1):
            if num%i == 0:
                tmp_num += i
        if tmp_num == num + 1:
            return True
        else:
            return False

    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer

solution('122312')


# Time error

def solution1(number):
    import itertools
    
    def check(num):
        tmp_num = 0
        for i in range(2, num+1):
            if num%i == 0:
                tmp_num += i
        if tmp_num == num:
            return True
        else:
            return False
    
    num_lst= list(number)
    num_lst_str_combi = []

    for pick in range(1, len(number)+1):
        num_lst_str = list(map(''.join, itertools.permutations(num_lst, pick)))  
        num_lst_str_combi.extend(set(num_lst_str)) 
        
    num_lst_int = list(map(int, num_lst_str_combi))
    num_lst_check = list(map(check, set(num_lst_int)))

    return num_lst_check.count(True)

solution1('011')


# After time error.
# Used set function

def solution1(number):
    import itertools
    
    def check(num):
        tmp_num = 0
        for i in range(1, num+1):
            if num%i == 0:
                tmp_num += i
        if tmp_num == num + 1:
            return True
        else:
            return False
    
    num_lst= list(number)
    num_lst_str_combi = []

    # set으로 중복을 제거했다.

    for pick in range(1, len(number)+1):
        num_lst_str = set(list(map(''.join, itertools.permutations(num_lst, pick)))) 
        for each_case in num_lst_str:
            if check(int(each_case)) == True:
                num_lst_str_combi.append(int(each_case)) 
    
    return len(set(num_lst_str_combi))

solution1('011')

