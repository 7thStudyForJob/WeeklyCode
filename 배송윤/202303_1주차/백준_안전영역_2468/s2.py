import sys
from collections import deque
sys.stdin = open('input.txt')


def DFS(height, start):
    stack = deque()
    stack.append(start)

    # 방문처리 위한 배열

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >=0 and ny < N:
                if not visited[nx][ny] and location[nx][ny] > height:
                    visited[nx][ny] = True
                    stack.append([nx, ny])     
    return


N = int(input())

location = []
# maxx = 0 으로 두면 모든 높이가 1인 경우, 비가 오지 않았을 때 답은 1인데 0이된다.
maxx = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
for _ in range(N):
    row = list(map(int, input().split()))
    location.append(row)
    tmp = max(row)
    if tmp > maxx:
        maxx = tmp


for i in range(0, maxx+1):
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and location[x][y] > i :
                visited[x][y] = False
                DFS(i, [x,y])
                cnt += 1
    if answer <= cnt:
        answer = cnt
print(answer) 

   


