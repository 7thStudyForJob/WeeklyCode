import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x==M-1 and y==N-1 :
        return 1

    elif visited[x][y] != -1 :
        return visited[x][y]

    else :
        visited[x][y] = 0
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<M and 0<=ny<N and maps[nx][ny] < maps[x][y] :
                visited[x][y] += dfs(nx,ny)

        return visited[x][y]

M,N = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(M)]
visited = [[-1]*N for _ in range(M)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

print(dfs(0,0))