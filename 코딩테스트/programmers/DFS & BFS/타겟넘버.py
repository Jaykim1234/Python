
"""
타겟 넘버
문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
입출력 예
numbers	target	return
[1, 1, 1, 1, 1]	3 5
입출력 예 설명
문제에 나온 예와 같습니다.
"""

from collections import deque
def bfs(input_lst, target):

    queue = deque()
    queue.append([ input_lst[0], 0])
    queue.append([-input_lst[0], 0])

    n = len(input_lst)
    count = 0
    idx   = 0
    while queue :
        tmp, idx  = queue.popleft()
        idx +=  1
        if idx < n:
            queue.append([tmp + input_lst[idx],  idx])
            queue.append([tmp - input_lst[idx],  idx])
        else:
            if tmp == target :
                count += 1
    return count

bfs([1, 1, 1, 1, 1], 3)

def dfs(number, target):
    if sum(number)== target:
        pass
    





# 다른 사람 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


# def test(lst):
#     if not lst:
#         print('empty')
#     else:
#         print('not empty')

# test([])