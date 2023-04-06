import sys
sys.stdin = open('input.txt')

from collections import deque
import copy

def make_wall(count):
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 0:
                lab_map[i][j] = 1
                make_wall(count+1)
                lab_map[i][j] = 0
                

def bfs():
    tmp_map = copy.deepcopy(lab_map)
    q = deque()
    # 2 좌표 담기
    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 2:
                q.append((i, j))
    
    # 바이러스 퍼뜨리기
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if tmp_map[nx][ny] == 0:
                    tmp_map[nx][ny] = 2
                    q.append((nx, ny))
    
    count_zero(tmp_map)

# 0 세기
def count_zero(tmp_map):
    global answer
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_map[i][j] == 0:
                cnt += 1  
    
    if answer < cnt:
        answer = cnt

    

N, M = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(N)]
# 세운 벽 갯수
wall_count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

make_wall(wall_count)

print(answer)

