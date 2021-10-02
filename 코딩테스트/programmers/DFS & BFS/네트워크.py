
"""
네트워크
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

입출력 예 설명
예제 #1
아래와 같이 2개의 네트워크가 있습니다.
image0.png

예제 #2
아래와 같이 1개의 네트워크가 있습니다.
image1.png
"""


def solution(n, computers):
    visit = [False for i in range(n)]
    ans = 0
    for cur in range(n):
        if visit[cur] == False:
            dfs(n, computers, visit, cur)
            ans += 1
    return ans

def dfs(n, computers, visit, cur):
    visit[cur] = True
    for s_idx in range(n):
        if computers[cur][s_idx] == 1 and s_idx != cur and  visit[s_idx] == False:
            dfs(n, computers, visit, s_idx)


    

    




# def solution(n, computer):
#     visited = [False for idx in range(n)]
#     answer  = 0
#     for com in range(n):
#         if  visited[com] == False:
#             bfs(n, computer, com, visited)
#             answer += 1
#     return  answer

# def bfs(n, computer, com, visited):
#     visited[com] = True
#     queue = []
#     queue.append(com) 
#     while len(queue) != 0:
#         com =  queue.pop(0)
#         visited[com] = True
#         for connect in range(n):
#             if connect != com and computer[com][connect] == 1 :
#                 if visited[connect] == False:
#                 # computer[cur_com][connection] == 2
#                     queue.append(connect)


# solution(4, [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 0], [1, 0, 1, 1]])

# def BFS(n, computers, com, visited):
#     visited[com] = True
#     queue = []
#     queue.append(com)
#     while len(queue) != 0:
#         com = queue.pop(0)
#         visited[com] = True
#         for connect in range(n):
#             # 자기 자신을 제외하고 다른 곳에서 1을 가지면
#             if connect != com and computers[com][connect] == 1:
#                 if visited[connect] ==  False:
#                     queue.append(connect)

# def solution(n, computers):
#     answer = 0
#     visited = [False for i in range(n)] # False False False  ~~
#     for com in range(n): # com : 지금 현재의 섬 인덱스
#         if visited[com] == False:
#             BFS(n, computers, com, visited)
#             answer += 1
#     return answer



# solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])


# from collections import deque
# def solution(n, visit):
#     total_comwork = [] 
#     index = 0
#     queue = deque()

#     while index < n:
#         queue.append([idx for idx  in range(1, n) if visit[index][idx-1] == 1])
#         total_comwork.append(queue.leftpop())
#         index +=  1
        
#         if index <= n-1:
#             new_comwork  = [idx for idx  in range(1, n) if visit[index][idx-1] == 1] 

#         index_2 = 0

#         while index_2 < n:
#             common_comwork  = [i for i in new_comwork if  total_comwork[index_2]]
            
#             if common_comwork:
#                 total_comwork[index_2] = list(set(total_comwork[index_2].extend[new_comwork]))
#                 break
#             else:
#                 total_comwork.append([new_comwork])
#             index_2 += 1
        
#     return total_comwork

# solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])


# def solution(n, visit):
#     total_comwork = [] 
#     index = 0

#     while index < n:
#         total_comwork.append([visit[index]])
#         index +=  1
#         new_comwork  = visit[index] # [ 2, 3 ]

#         index_2 = 0

#         while index_2 < n:
#             common_comwork  = [i for i in new_comwork if  total_comwork[index_2]]
            
#             if common_comwork:
#                 total_comwork[index_2] = list(set(total_comwork[index_2].extend[new_comwork]))
#                 break
#             else:
#                 total_comwork.append([new_comwork])
#             index_2 += 1
        
#     return total_comwork

# solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])

# from collections import deque
# def solution(n, visit):
#     queue  = deque()
#     total_comwork = [] 
#     index = 0
#     n = len(visit)
#     while index < n:
#         queue.append(visit[index])
#         current_comwork = queue.popleft()
#         total_comwork.append([current_comwork])
#         new_comwork      = visit[index] # [ 2, 3 ]

#         for each_comwork in total_comwork:
#             common_comwork   = [i for i in new_comwork if i in current_comwork]

#             if common_comwork:
#                 current_comwork= list(set(current_comwork.extend[new_comwork]))
#             else:
#                 total_comwork.append([new_comwork])

#         index +=  1
        
#     return total_comwork


print(type(set([1,2,2,2,2,3])))
print(type(list(set([1,2,2,2,2,3,2]))))

# from collections import deque
# def solution(n, visit):
#     queue  = deque()
#     queue.append([idx for idx  in range(1, n) if visit[0][idx-1] == 1])   # [ 1, 2 ] 
#     index = 1
#     n = len(visit)
#     while index < n-1:
#         previous_comwork = queue.popleft()
#         new_comwork      = [idx_1 for idx_1  in range(1, n) if visit[index][idx_1-1] == 1] # [ 2, 3 ]
#         common_comwork   = [i for i in new_comwork if i in previous_comwork]
        

#         index += 1
#         if 


#         extended_comwork = [i for i in new_comwork if i not in previous_comwork ]





    # for case in visit: # case: [1, 1, 0]
    #     if lock == 1:
    #         total_com.extend([idx for idx in range(1, n) if case[idx-1] == 1])
    #         lock -= 1
    #     else:
    #         cur_com = [idx for idx in range(1, n) if case[idx-1] == 1]





