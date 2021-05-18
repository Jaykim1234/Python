# n,m = 4,6

# situation0 = [
# 	[1,1,0,1,1,0], 
# 	[1,1,0,1,1,0],
# 	[1,1,1,1,1,1],
# 	[1,1,1,1,0,1]
# 	] 
	
# situation = [
# 	[1,0,1,1,1,1], 
# 	[1,0,1,0,1,0],
# 	[1,0,1,0,1,1],
# 	[1,1,1,0,1,1]
# 	] 

from sys import stdin
n, m = map(int, stdin.readline().split())
# matrix 배열
situation = [stdin.readline().rstrip() for _ in range(N)]


m_r = [-1,0,1,0]
m_c = [0,1,0,-1]

min_count = n*m


import copy

def move(row, col, depth ,sit):
	
	global min_count
	
	if row == n-1 and col == m-1:
		min_count = min(depth, min_count)
		print(min_count, depth)
		return 

	for index in range(4):
		new_row = row + m_r[index]
		new_col = col + m_c[index]

		if (0 <= new_row <= n-1) and (0 <= new_col <= m-1):
			if sit[new_row][new_col] == 1:
				print(sit)
				sit[new_row][new_col] = 2
				
				move(new_row, new_col, depth+1, sit)
				sit[new_row][new_col] = 1
			
move(0,0,1,situation)
print(min_count)



# situation = [
#     [1,0,1,1,1,1],
#     [1,0,1,0,1,0],
#     [1,0,1,0,1,1],
#     [1,1,1,0,1,1]
#     ]

# blank_spot =  [
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]
#     ]

# spots = [[i,j] for i in range(6) for j in range(4)]

# wall_spots = []
# min_move_count = 4*6

# for n in range(4):
#     for m in range(6):
#         if situation[n][m] == 0:
#             wall_spots.append([n,m])

# # moving

# m_r = [1,0,-1,0]
# m_c = [0,-1,0,1]

# def spread(row,col,sit):
#     if sit[row][col] == 1:
#         for i in range(4):
#             new_row = row + m_r[i]
#             new_col = col + m_c[i]
    
#             if new_row >= 0 and new_row < 4 and new_col >= 0 and new_col < 6:
#                 if sit[new_row][new_col] == 1:
#                     spread(new_row,new_col,sit)


# def check_point(start,count):
    
#     global min_move_count
    
#     if count == 3 : 
#             copied_situation = copy.deepcopy(situation) # Make copied version of situation
#             for num in range(len(virus_spots)):
#                 r, c = virus_spots[num]
#                 spread(r, c, copied_situation)
#             move_counts = sum(i.count(0) for i in copied_situation) 
#             max_virus_count = max(max_virus_count,safe_counts)
#             return True

#     for i in range(start, N*M):
#         row = i // M
#         col = i % M
#         if situation[row][col] == 1 : 
#             situation[row][col] = 'm' 
#             select_wall(i,count+1) # 여기서 if == 3으로 들어간다.
#             situation[row][col] = 0


from sys import stdin

N,M = 4,6

matrix = [
	[1,1,0,1,1,0], 
	[1,1,0,1,1,0],
	[1,1,1,1,1,1],
	[1,1,1,1,0,1]
	] 
	
# situation = [
# 	[1,0,1,1,1,1], 
# 	[1,0,1,0,1,0],
# 	[1,0,1,0,1,1],
# 	[1,1,1,0,1,1]
# 	] 

# N, M = map(int, stdin.readline().split())
# # matrix 배열
# matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
visited = [[0]*M for _ in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0)]
visited[0][0] = 1

while queue:
    	
		x, y = queue.pop(0)
		print(x,y)

		if x == N-1 and y == M-1:
			# 최종 경로 도착
			print(visited[x][y])
			break

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < N and 0 <= ny < M:
				if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
					visited[nx][ny] = visited[x][y] + 1
					queue.append((nx,ny))