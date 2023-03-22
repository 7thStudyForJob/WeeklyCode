import sys; sys.stdin=open("톱니바퀴.txt")
# 1, 2, 3, 4번 바퀴
# k번 회전
# 회전 방향 (시계, 반시계)
# A가 회전할때, 그 전에 서로 맞닿은 (반대의) 극이 다르다면, B가 반대로 한번 회전
# index 활용

# 입력 1,2,3,4 시계방향 8개, N = 0 , S = 1, 이후 K , (톱니번호, 방향 1=시계, -1=반시계)
wheel = []
for i in range(4):
    wheel.append(list(map(int, input())))

leftAndright = [(6, 2)] * 4
def DFS(n, d):
    global visit
    visit[n] = True

    left, right = leftAndright[n]
    # 우측확인
    if n+1 < 4 and not visit[n+1]:
        nextleft, nextright = leftAndright[n+1]
        if wheel[n][right] != wheel[n+1][nextleft]:
            DFS(n+1, -d)
    # 좌측확인
    if n-1 >= 0 and not visit[n-1]:
        nextleft, nextright = leftAndright[n-1]
        if wheel[n-1][nextright] != wheel[n][left]:
            DFS(n-1, -d)
    # 회전
    # 시계 (index 반대)
    if d == 1:
        leftAndright[n] = ((left + 7) % 8, (right + 7) % 8)
    else:
        leftAndright[n] = ((left + 1) % 8, (right + 1) % 8)

K = int(input())
visited = [False] * 4
for _ in range(K):
    n, d = map(int, input().split())
    visit = visited.copy()
    # index
    DFS(n-1, d)

# 점수
score = 0
for i in range(4):
    top = (leftAndright[i][0] + 2) % 8
    if wheel[i][top] == 1:
        score += 2 ** i

print(score)