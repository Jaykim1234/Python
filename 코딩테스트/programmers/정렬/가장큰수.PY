
"""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
"""

lst =[3, 30, 34, 5, 9]


def solution(lst):
    ans_num = ''

    for round in range(len(lst)):
        tmp = ''
        while True:
            

    


def solution(lst):
    lst2 = list(map(str, lst))
    import itertools
    npr = list(itertools.permutations(lst2, len(lst)))
    print(npr)
    npr2= list(map(''.join, npr))
    print(npr2)
    npr3 = list(map(int, npr2))
    print(npr3)
    return max(npr3)
solution([3, 30, 34, 5, 9])



# Time error
def solution2(lst):
    import itertools
    lst2 = list(map(str, lst))
    npr = list(map(''.join, list(itertools.permutations(lst2, len(lst)))))
    return max(npr)
solution2([3, 30, 34, 5, 9])


def solution3(lst):
    result_num = ''
    start_num = 0 
    for index in range(0, len(lst)):
        start_num = max(start_num, int(str(lst[index])[0]))
    result_num += str(start_num)
    return result_num

solution3([3, 30, 34, 5, 9])
