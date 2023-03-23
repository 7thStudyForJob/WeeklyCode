import sys
from collections import deque
sys.stdin = open('input.txt')

# 모두 익었는지 확인 할 함수
def check_ripe(graph):
    for i in range(N):
        for j in range(M):
            # 하나라도 익지 않은 것이 있다면 False
            if graph[i][j] == 0:
                return False
                
    return True

# 토마토를 익히자
def bfs(start):
    global day
    q = deque()
    
    for s in start:
        q.append(s)
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while q:
        x, y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < N and ny >=0 and ny < M:
                if graph[nx][ny] == 0:
                    # 인접 토마토가 익은 날짜에 +1을 하여 nx,ny에 있는 토마토가 익은 날짜 표시
                    graph[nx][ny] = graph[x][y] + 1
                    # 마지막 토마토가 익은 날짜 갱신
                    day = graph[nx][ny]
                    q.append([nx, ny])


M, N = map(int, input().split())
start = []
day = 0
graph = []
all_ripe = True

# 토마토 상자 채우기
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 시작점 찾기 
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            # 시작점이 여러개 일 수 있다.
            start.append([i, j])
        # 만약 0이 하나도 없다면 모든 토마토가 다 익었다는 뜻.
        elif graph[i][j] == 0:
            all_ripe = False

# 모든 토마토가 익은 경우
if all_ripe:
    print(0)
# 하나라도 익지 않은게 있다면 탐색
else:
    bfs(start)

    # 모든 토마토가 익었는지 확인
    if check_ripe(graph):
        print(day-1)
    else:
        print(-1)