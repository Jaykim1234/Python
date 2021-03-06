"""
조이스틱
문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
"JEROEN"	56
"JAN"	    23
"""

# 위 아래 방향 찾기
# 좌 우 최적 값 찾기

# 02-13 다시 풀기

inp_string = "BBABAB"


def solution(inp_string):
    ud_change = [ min((ord(i) - ord('A')), (ord('Z')- ord(i)+1)) for i in inp_string]
    idx, answer = 0, sum(ud_change)

    if answer == 0:
        return 0

    while True:
        left, right = 1, 1

        while inp_string[idx - left] == 'A':
            left += 1

        while inp_string[idx + right] == 'A':
            right += 1

        answer += left if left == min(left, right) else right
        idx += -left if left == min(left, right) else right 

    return answer

solution(inp_string)

# https://jokerldg.github.io/algorithm/2021/05/24/joystick.html


# def solution(ans_string):
#     a_string = 'A'*len(ans_string)
#     idx = 0
#     while a_string != ans_string:
#         if ans_string[idx] == a_string[idx]:
#             idx += 1
#             answer += 1
#         while ans_string[idx] == a_string[idx]:
#             idx += 1
#             answer += 1 
# solution(ans_string)
        






# def r_left(string, idx):
#     directions = [-1, 1]
#     count_lst = []

#     for direction in directions:
#         count = 0
#         while string[idx] != 'A':
#             idx += direction
#             count += 1
#             if idx == len(string):
#                 idx = 0
#             elif idx < 0:
#                 idx = len(string) -1
#         count_lst.append([count,idx])

#     return  count_lst[0] if count_lst[0][0] > count_lst[1][0] else count_lst[1]

# def updown(string, idx, check):
#     count = 0
#     check[idx] = True
#     if (ord(string[idx]) - ord('A')) < (ord('Z')- ord(string[idx])):
#         count += ord(string[idx]) - ord('A')
#     else:
#         count += ord('Z')- ord(string[idx]) + 1
#     return count, check

# def solution(string):
#     count = 0
#     check = [False if s != 'A' else True for s in string]
    
#     if set(check) == {True}:
#         return 0
#     idx = 0
#     while set(check) != {True}:
#         add_hori, idx = r_left(string, idx)
#         add_ud, check  = updown(string, idx, check)
#         count += add_hori + add_ud
#     return count

# print(solution("JEROEN"))

#    current_loc = [0 if string[i] != 'A' else 1 for i in range(len(string)) ]
    # idx_lst = [idx for idx in range(len(string)) if string[idx] != 'A' ]
    # for idx_1 in range(len(idx_lst)):
    #     if idx_1 + 1 != len(idx_lst):
    #         if (idx_lst[idx_1+1] - idx_lst[idx_1]) < len(string)
    #     else:
    #         if idx`` 

# def updown(idx, string):
#     count = 0
#     if (ord(string[idx]) - ord('A')) < (ord('Z')- ord(string[idx])):
#         count += ord(string[idx]) - ord('A')
#     else:
#         count += ord('Z')- ord(string[idx]) + 1
#     return count


       

# location = [0 if i == 'A' else 1 for i in string]

# def solution(string):

# string = "JEROEN"
# [0 if i == 'A' else '1' for i in string]


# print(ord('J')- ord('A'))
# print(ord('N')- ord('A'))
# print(ord('Z')- ord('N'))