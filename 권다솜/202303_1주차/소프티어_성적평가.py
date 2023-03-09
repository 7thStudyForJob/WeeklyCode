import sys

# 참가자의 수
N = int(input())

# 대회 결과
contestScore = [list(map(int,input().split())) for _ in range(3)]
contestScore.append([])

# 총 3개 대회의 합계
for i in range(N):
    total = contestScore[0][i] + contestScore[1][i] + contestScore[2][i]
    contestScore[3].append(total)

scoreToRank = [{},{},{},{}]
result = [[],[],[],[]]

num = 0
# 등수 정리하기
for contest in contestScore:
    # 점수를 내림차순으로 정렬
    score = sorted(contest,reverse=True)

    # 정렬된 점수를 통해 해당 점수의 등수 지정
    for i in range(N):
        keyV = score[i]
        # 이미 있는 점수이면 건너뜀
        if keyV in scoreToRank[num].keys():
            continue
        
        # 해당 점수의 등수가 없으면 새로 등록
        scoreToRank[num][keyV] = i+1
    
    # 등수 정의표를 통해 해당 점수를 등수로 변환한다.
    for i in contest:
        rank = scoreToRank[num][i]
        result[num].append(rank)
    
    num += 1

# 결과값 출력
for i in result:
    print(*i)
