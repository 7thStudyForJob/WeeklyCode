import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(N)]

visited = [[[0]*M for _ in range(N)] for _ in range(2)]

def bfs(start):
    queue = deque([start])

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    visited[0][start[1]][start[2]] = 1

    while queue:
        pc,x,y = queue.popleft()
        if x==N-1 and y==M-1:
            return visited[pc][x][y]

        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]

            if 0<=nx<N and 0<=ny<M and visited[pc][nx][ny]==0:
                # 벽이 아닌 곳을 만났다면
                if arr[nx][ny] == 0:
                    queue.append([pc,nx,ny])
                    visited[pc][nx][ny] = visited[pc][x][y]+1
                # 그런데 벽을 만났다면
                else:
                    if pc==1:
                        continue
                    queue.append([1,nx,ny])
                    visited[1][nx][ny] = visited[pc][x][y] + 1


ans = bfs([0,0,0])
if ans == 0 or ans == None:
    print(-1)
else:
    print(ans)