import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# swea방식에 익숙해서...
T = int(input())
for tc in range(T):
    n = int(input())
    # n*n의 2차원 영행렬
    arr = [[0]*n for _ in range(n)]
    # 학생수*4의 2차원 행렬
    students = [list(map(int, input().split())) for _ in range(n*n)]

    # 학생 수 만큼 이하를 실행
    for i in range(n*n):
        student = students[i]
        # 여기다가 가능한 자리를 다 담아서 정렬 후 앉힘
        tmp = []
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    like = 0
                    blank = 0
                    for k in range(4):
                        nr, nc = i + dr[k], j + dc[k]
                        # n*n행렬 안이어야지
                        if 0 <= nr < n and 0 <= nc < n:
                            # 좋아하는 학생(각 행 리스트의 인덱스 1에서 4까지)이 상하좌우 안에 있다면
                            if arr[nr][nc] in student[1:]:
                                like += 1
                            # 4방향 안에 아무도 없다면
                            if arr[nr][nc] == 0:
                                blank += 1
                                # 각 포인트에서 like의 수, blank의 수, 좌표를 tmp에 추가해주자
                    tmp.append([like, blank, i, j])
        # 첫 번째로 like를 내림차순, 두 번째로 blank를 내림차순, 세 번째로 i를 오름차순, 네 번째로 j를 오름차순
        tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
        # 제일 많은 like, 제일 많은 blank가, 제일 적은 i가, 제일 적은 j가 있는 tmp의 0번째 행의 i와 j에 학생을 앉히자
        arr[tmp[0][2]][tmp[0][3]] = student[0]
        
    satisfactions = 0
    # 학생 번호 오름차순으로 fot문 돌리기 위해 학생 번호 오름차순 정렬
    students.sort()

    for i in range(n):
        for j in range(n):
            # 좋아하는 학생 수 변수 설정
            preferfriend = 0
            for k in range(4):
                nr, nc = i + dr[k], j + dc[k]
                # 행렬 안에서
                if 0 <= nr < n and 0 <= nc < n:
                    # 주변 친구의 번호가 
                    # students(input으로 받아온 2차원 행렬의 첫번째 값을 기준으로 오름차순 정렬)
                    # 에 있는 학생 arr[i][j]의 students에서의 인덱스(학생의 번호-1)에 존재하는 1차원 행렬의 안에 있다면
                    if arr[nr][nc] in students[arr[i][j]-1]:
                        # preferfriend에 1을 더해줘라
                        preferfriend += 1
            # preferfriend가 0이 아니라면 만족도를 계산해서 satisfactions에 더해줘
            if preferfriend:
                satisfactions += 10 ** (preferfriend-1)
    print(satisfactions)
