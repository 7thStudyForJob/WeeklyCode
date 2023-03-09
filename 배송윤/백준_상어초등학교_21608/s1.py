import sys
sys.stdin = open('input.txt')

def satisfy(dict):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    summ = 0
    for r in range(N):
        for c in range(N):
            cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr >= 0 and nr < N and nc >= 0 and nc < N:
                    if graph[nr][nc] in dict.get(graph[r][c]):
                        cnt += 1
            if cnt > 0:
                summ += 10**(cnt-1)
    return summ

def search(student, likeList):
    # 상, 우, 하, 좌 순으로 탐색
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    best = -1

    for r in range(N):
        for c in range(N):
            like = 0 
            emp = 0
            if graph[r][c] == 0:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr >= 0 and nr < N and nc >= 0 and nc < N:
                        if graph[nr][nc] == 0:
                            emp += 1
                        elif graph[nr][nc] in likeList:
                            like += 2      
                summ = emp+like
                if best < summ:
                    best = summ
                    x = r
                    y = c
    
    graph[x][y] = student
    
    pass

N = int(input())
graph = [[0]*N for _ in range(N)]
dict = {}

for i in range(N**2):
    arr = list(map(int, input().split()))
    dict[arr[0]] = arr[1:]    
    search(arr[0], arr[1:])

answer = satisfy(dict)
print(answer)
