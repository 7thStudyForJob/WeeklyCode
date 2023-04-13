import sys
sys.stdin = open('input.txt')

# ㅗ 모양 나머지 블록은 DFS로 하나씩 탐색해나가며 4개의 위치를 탐색하는 것과 같다.
def dfs(x, y, cnt, summ):
    global answer
    if cnt > 3:
        answer = max(answer, summ)
        summ = 0
        return

    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]

        if 0<=nx<N and 0<=ny<M:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                # 이 재귀를 통해 한쪽 방향 끝으로 갔다가, 방향 바꿔가면서 4칸 방문
                dfs(nx, ny, cnt+1, summ+graph[nx][ny])
                visited[nx][ny] = False

def purple(x, y):
    global answer
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = graph[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+dir[t][0]
            nj = j+dir[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += graph[ni][nj]
        # 최대값 계산
        answer = max(answer, tmp)



N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range (N)]
answer = 0
cnt = 0
summ = 0
# 상 우 하 좌
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[False] * M for _ in range(N)]
# print(visited)
# 반복문으로 놓을 수 있는 곳을 찾고
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j, cnt, summ)
        visited[i][j] = False
        purple(i,j)

print(answer)

