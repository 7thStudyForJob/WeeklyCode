import sys; sys.stdin=open("상어초등학교.txt")

N = int(input())
answer = 0
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

students = []
like_students = [[] for _ in range(N ** 2 + 1)]
for i in range(N**2):
    info = list(map(int, input().split()))
    students.append(info)
    like_students[info[0]].append(info[1:])

arr = [[0] * N for _ in range(N)]
for i in range(N**2):
    temp = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] != 0: continue
            like = 0
            empty = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                if arr[nx][ny] in students[i][1:]:
                    like += 1
                if arr[nx][ny] == 0:
                    empty += 1
            temp.append((like, empty, (x,y)))
    temp.sort(key = lambda x : (-x[0], -x[1], x[2]))
    arr[temp[0][2][0]][temp[0][2][1]] = students[i][0]

for i in range(N):
    for j in range(N):
        check = arr[i][j]
        cnt = 0
        for z in range(4):
            nx = i + dx[z]
            ny = j + dy[z]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if arr[nx][ny] in like_students[check][0]:
                cnt += 1

        if cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        elif cnt == 4:
            answer += 1000

print(answer)