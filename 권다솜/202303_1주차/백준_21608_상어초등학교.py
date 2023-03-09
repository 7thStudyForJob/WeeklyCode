N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

studentsList = [list(map(int,input().split())) for _ in range(N**2)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for num in range(N**2):
    # 학생 정보
    studentInfo = studentsList[num]

    possible = []
    for i in range(N):
        for j in range(N):
            # 1.빈자리인지 확인한다.
            if arr[i][j] == 0:
                likeCnt = 0
                emptyCnt = 0

                # 2.상하좌우를 살핀다.
                for k in range(4):
                    DX,DY = i + dx[k], j + dy[k]

                    if DX >= N or DX < 0 or DY >= N or DY < 0:
                        continue
                    
                    # 3.상하좌우에 좋아하는 학생이 있는지 찾는다.
                    if arr[DX][DY] in studentInfo[1:]:
                        likeCnt += 1

                    # 4.상하좌우에 빈공간이 있는지 찾는다.
                    if arr[DX][DY] == 0:
                        emptyCnt += 1

                # 5.앉을 수 있는 자리 목록에 넣어준다.
                possible.append([likeCnt,emptyCnt,i,j])
    
    # 6.앉을 수 있는 자리 목록을 좋아하는 학생 수가 가장 많고, 빈자리가 많으며, 행의 번호가 작은 순서로 나열한다.
    possible.sort(key= lambda x:(-x[0],-x[1],x[2],x[3]))

    # 7.학생을 앉힌다.
    arr[possible[0][2]][possible[0][3]] = studentInfo[0]

result = 0
studentsList.sort()
for i in range(N):
    for j in range(N):
        # 학생 정보
        studentInfo = studentsList[arr[i][j]-1]
        # 좋아하는 학생 수
        cnt = 0
        for k in range(4):
            DX,DY = i + dx[k], j + dy[k]

            if DX >= N or DX < 0 or DY >= N or DY < 0:
                continue

            if arr[DX][DY] in studentInfo:
                cnt += 1
        
        # 결과값 업데이트
        if cnt != 0:
            result += 10**(cnt-1)

print(result)