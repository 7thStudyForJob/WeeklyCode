N = int(input())

students = {}
for _ in range(N**2):
    number,*lst = list(map(int,input().split()))
    students[number] = lst

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def check_around(loc,friend_lst):
    friend_cnt = 0
    empty_cnt = 0

    x,y = loc
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]

        if 0<=nx<N and 0<=ny<N:
            if seat[nx][ny] == 0:
                empty_cnt += 1
            else:
                if seat[nx][ny] in friend_lst:
                    friend_cnt += 1
    return friend_cnt,empty_cnt



# 자리배열
seat = [[0]*N for _ in range(N)]

# 자리 배치하기
for me,friends in students.items():
    friend_maximum = -1
    empty_maximum = -1
    my_seat = (0,0)

    # 지금 학생의 자리 정하기
    for i in range(N):
        for j in range(N):
            # 빈자리라면
            if seat[i][j] == 0:
                # 인접 자리 탐색해서, 좋아하는 친구들 수와 빈자리 수 확인
                friend_cnt,empty_cnt = check_around((i,j),friends)
                # 인접 친구 수가 많으면
                if friend_cnt>friend_maximum:
                    friend_maximum = friend_cnt
                    empty_maximum = empty_cnt
                    my_seat = (i,j)
                # 친구 수가 같으면
                elif friend_cnt == friend_maximum:
                    # 빈자리로 테스트
                    if empty_cnt > empty_maximum:
                        empty_maximum = empty_cnt
                        my_seat = (i,j)
    seat[my_seat[0]][my_seat[1]] = me

# 만족도 구하기
score = 0
for i in range(N):
    for j in range(N):
        student_no = seat[i][j]
        friend_cnt, empty_cnt = check_around((i,j),students[student_no])
        if friend_cnt:
            score += 10**(friend_cnt-1)

print(score)