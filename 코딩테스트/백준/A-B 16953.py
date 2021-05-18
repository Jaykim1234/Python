# from sys import stdin
N, M = map(int, input().split())


# BFS 경로 탐색
# queue 방식 사용
queue = [(2*N, 10*N + 1)]
count = 0

while queue: # queue에 원소가 남아있을 때까지 진행
    multiple, add = queue.pop(0)

    count += 1

    if M in (multiple, add):
        # 최종 경로 도착
        print(count)
        break

    if min(multiple, add) > M:
        print('over')
        break

    queue.append((2*multiple, 10*multiple +1))
    print('gogogoogog')
    queue.append((2*add, 10*add +1))

print(-1)

# queue = [1,2,3,4,5]

# while queue:
#     x =  queue.pop(0)
#     print(x)

# rint( 5 in (6,8))