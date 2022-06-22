
def check(key, y, x):
    ret = True
    M = len(key)
    
    for i in range(y, y + M):
        for j in range(x, x+M):
            board[i][j] += key[i-y][j-x]

    for i in range(M, M+N):
        for j in range(M,M+N):
            if board[i][j] != 1:
                ret = False
                break
        if ret : break
    
    for i in range(y,y+M):
        for j in range(x,x+M):
            board[i][j] -=key[i-y][j-x]
    
    return ret

key  = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate(key):
    M    = len(key)
    
    temp = [[] for i in range(M)]

    for i in range(M):
        for j in range(M):
            temp[i][j] = key[j][M-i-j]

    for i in range(M):
        for j in range(M):
            key[i][j] = temp[i][j]

    return key

def solution(key, lock):
    answer = False

    M = len(key)
    N = len(lock)

    board = [[] for i in range(N+M)]

    for i in range(M+N):
        for j in range(M+N):
            board[i][j] = lock[i-M][j-M]

    for i in range(N+M):
        for j in range(N+M):
            for j in range(4):
                rotate(key)
                if check(key, M, N):