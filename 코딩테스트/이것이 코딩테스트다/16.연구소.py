# N,M = 7,7
# situation =[[2 ,0 ,0 ,0 ,1 ,1 ,0],[0 ,0 ,1 ,0 ,1 ,2 ,0],[0 ,1 ,1 ,0,1 ,0, 0],[0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 1],[0, 1, 0, 0, 0, 0, 0],[0, 1, 0 ,0 ,0 ,0, 0]]
# spots = [(i,j) for i in range(N) for j in range(M)]
# virus_spots= []
# wall_spots = []

# location = [-1,-1]
# for row in situation:
#     location[0] += 1
#     for i in row:
#         location[1] += 1
#         if location[1] >= M:
#             location[1] -= M
#         if i == 2:
#             virus_spots.append(tuple(location)) # tuple을 안쓰면 외부변수가 바뀌면 내부 변수도 같이 변한다!! 
#         elif i == 1:
#             print(1)
#             wall_spots.append(tuple(location))
#         else:
#             pass
# # print(virus_spots)
# # print(wall_spots)

# for i in virus_spots:
#     i = moving_spot
     




# lst= []
# test_lst=[1,2]
# lst.append(test_lst)
# print(lst)
# test_lst.pop()

# print(lst)



# N,M = 7,7
# situation =[[2 ,0 ,0 ,0 ,1 ,1 ,0],[0 ,0 ,1 ,0 ,1 ,2 ,0],[0 ,1 ,1 ,0,1 ,0, 0],[0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 1],[0, 1, 0, 0, 0, 0, 0],[0, 1, 0 ,0 ,0 ,0, 0]]
# spots = [[i,j] for i in range(N) for j in range(M)]
# virus_spots= []
# wall_spots = []

# # virus

# for n in range(N):
#     for m in range(M):
#         if situation[n][m] == 2:
#             virus_spots.append[[n,m]]
#         elif situation[n][m] == 2:
#             wall_spots.append[[n,m]]
#         else:
#             pass

# #문제 풀이과정
# '''
# 1. 벽을 선택한다.
# 2. 바이러스를 퍼트린다.
# 3. 바이러스가 퍼지지 않은 안전지역 면적을 구한다.
# 1~3번의 과정을 벽을 선택하는 모든 경우의 수에 대해서 반복하고, 
# 마지막에 안전지역의 max값 리턴
# '''
 
# # input 및 변수선언
 
# import copy
# import sys
 
# input = sys.stdin.readline
 
# N, M = map(int, input().strip().split())
# NM = []
# for i in range(N):
#     L = list(map(int, input().strip().split()))
#     NM.append(L)
 
# dr = [-1,0,1,0] # 위아래 row 단위로 이동
# dc = [0,1,0,-1] # 좌우 column 단위로 이동
# max_value = 0 # clean 지역의 개수를 return 하기 위한 변수
# virus_list = [] # 바이러스 리스트 만들기
# for i in range(N):
#     for j in range(M):
#         if NM[i][j] == 2:
#             virus_list.append([i,j])
 
# # 벽 선택하기
# def select_wall(start,count):
#     global max_value
#     if count == 3 : # 종료조건, 벽 3개 선택 완료
#         sel_NM = copy.deepcopy(NM) # deepcopy로 벽이 선택된 배열 복사
#         for num in range(len(virus_list)):
#             r, c = virus_list[num]
#             spread_virus(r, c, sel_NM)
#         safe_counts = sum(i.count(0) for i in sel_NM) # clean 지역 count
#         max_value = max(max_value,safe_counts)
#         return True
#     else :
#         for i in range(start, N*M): # 2차원 배열에서 조합 구하기
#             r = i // M
#             c = i % M
#             if NM[r][c] == 0 : # 안전영역인 경우 벽으로 선택가능
#                 NM[r][c] = 1 # 벽으로 변경
#                 select_wall(i,count+1) # 벽선택
#                 NM[r][c] = 0
 
 
# def spread_virus(r,c,sel_NM):
#     if sel_NM[r][c] == 2:
#         # 상하좌우 4방향을 확인하고 범위를 벗어나거나, 벽을만날때까지 반복
#         for dir in range(4):
#             n_r = r+dr[dir]
#             n_c = c+dc[dir]
#             if n_r >= 0 and n_c >=0 and n_r < N and n_c < M : # 범위를 벗어나지 않을때
#                 if sel_NM[n_r][n_c] == 0 :
#                     sel_NM[n_r][n_c] = 2
#                     spread_virus(n_r,n_c,sel_NM)
 
# # 메인
# select_wall(0,0)
# print(max_value)


# #출처: https://mentha2.tistory.com/24 [행궁동 데이터 엔지니어]

# # row_m = [-1,1]
# # col_m = [-1,1]
# # all_m = [row_m,col_m]

# # for i in virus_spots:
# #     while 

# for rows in situation:
#     if 2 in rows:
#         c_index = rows.index(2)
#         for index in list(range(len(rows))):
#             if c_index + 1 in list(range(len(rows))):
#                 if rows[c_index+1] = 0:
#                     rows[c_index+1] = 1
#             elif c_index - 1 in list(range(len(rows))):
#                 if rows[c_index-1] = 0:
#                     rows[c_index-1] = 1
#                 elif


# from collections import deque
# q = deque()
# q.append([1, 2])
# x, y = q.popleft()
# print(x,y)


# N,M = 7,7
# situation =[[2 ,0 ,0 ,0 ,1 ,1 ,0],[0 ,0 ,1 ,0 ,1 ,2 ,0],[0 ,1 ,1 ,0,1 ,0, 0],[0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 1],[0, 1, 0, 0, 0, 0, 0],[0, 1, 0 ,0 ,0 ,0, 0]]
# spots = [[i,j] for i in range(N) for j in range(M)]
# virus_spots= []
# wall_spots = []

# max_value = 0 

# dr = [1,0,-1,0]
# dc = [0,1,0,-1]

# for n in range(N):
#     for m in range(M):
#         if situation[n][m] == 2:
#             virus_spots.append([n,m])
#         elif situation[n][m] == 1:
#             wall_spots.append([n,m])
#         else:
#             pass

# def select_wall(start,count):
#     global max_value
#     while count < 3:
#         for i in range(start, N*M):
#             row = i//M
#             col = i%M
#             if situation[r][c] == 0:
#                 situation[r][c] = 1
#                 select_wall(i,count+1)
#                 situation[r][c] = 0
#     sel_NM = copy.deepcopy(situation)

#     for num in range(len(virus_list)):
#         row,col = virus_list[num]
#         spread_virus(r,c,sel_NM)
#     safe_counts = sum(i.count(0) for i in sel_NM)
#     max_value = max(max_value,safe_counts)
#     return True

# def spread_virus(row,col,sel_NM):
#     if sel_NM[row][col] == 2:
#         for dir in range(4):
#             n_r = r + dr[dir]
#             n_C = c + dc[dir]
#            if n_r >= 0 and n_c >=0 and n_r < N and n_c < M : 
#                 if sel_NM[n_r][n_c] == 0 :
#                     sel_NM[n_r][n_c] = 2
#                     spread_virus(n_r,n_c,sel_NM)

import copy
import sys
 
input = sys.stdin.readline
 
N, M = map(int, input().strip().split())
NM = []
for i in range(N):
    L = list(map(int, input().strip().split()))
    NM.append(L)
 
dr = [-1,0,1,0] 
dc = [0,1,0,-1] 
max_value = 0
virus_list = [] 
for i in range(N):
    for j in range(M):
        if NM[i][j] == 2:
            virus_list.append([i,j])
 
# 벽 선택하기
def select_wall(start,count):
    global max_value
    if count == 3 : 
        sel_NM = copy.deepcopy(NM) 
        for num in range(len(virus_list)):
            r, c = virus_list[num]
            spread_virus(r, c, sel_NM)
        safe_counts = sum(i.count(0) for i in sel_NM) 
        max_value = max(max_value,safe_counts)
        return True
    else :
        for i in range(start, N*M):
            r = i // M
            c = i % M
            if NM[r][c] == 0 : 
                NM[r][c] = 1 
                select_wall(i,count+1) 
                NM[r][c] = 0
 
 
def spread_virus(r,c,sel_NM):
    if sel_NM[r][c] == 2:
     
        for dir in range(4):
            n_r = r+dr[dir]
            n_c = c+dc[dir]
            if n_r >= 0 and n_c >=0 and n_r < N and n_c < M : 
                if sel_NM[n_r][n_c] == 0 :
                    sel_NM[n_r][n_c] = 2
                    spread_virus(n_r,n_c,sel_NM)


