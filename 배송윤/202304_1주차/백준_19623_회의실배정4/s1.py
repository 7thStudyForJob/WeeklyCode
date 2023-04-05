import sys
sys.stdin = open('input.txt')

N = int(input())
dp = [0] * (N+1)
time_table = [[0,0,0]] + [list(map(int, input().split())) for _ in range(N)]
time_table = sorted(time_table, key = lambda x : x[0])

# key = 끝나는 시간, val = 그 시간대에 가장 많은 인원
end_time = {}

# print(time_table)

for i in range(1, N+1):
    start, end, pple = time_table[i]
    maxx = 0
    # 끝나는 시간이 end인 시간대에 가장 많은 인원을 갱신한다.
    if end in end_time:
        end_time[end] = max(end_time[end], pple)
    
    else:
        end_time[end] = pple

    # 이전 회의의 끝나는 시간 이 현재 탐색중인 회의의 시작시간 보다 작거나 같은 값을 찾는다.
    for key, value in end_time.items():
        if start >= key:    
            maxx = max(maxx, end_time[key])
    
    end_time[end] += maxx   
    dp[i] = maxx + pple 


    # dp[i] = maxx + time_table[i][2]
#     print(dp)
# print(end_time)
# print(dp)
print(dp[-1])
        
# 10, 25, 80
            

# 회의를 이어 할 수 있는지 어떻게 알지

# [0, 0, 0], [10, 50, 50], [20, 120, 100], [30, 60, 60]



## 시간초과 ##
# N = int(input())
# dp = [0] * (N+1)
# time_table = [[0,0,0]] + [list(map(int, input().split())) for _ in range(N)]
# time_table = sorted(time_table, key = lambda x : x[0])

# print(time_table)

# for i in range(1, N+1):
#     start, end, pple = time_table[i]
#     maxx = 0
#     # 이전회의에 이어서 할 수 있는지 체크하기 위해, 처음 부터 탐색한다.
#     for j in range(i):
#         # 지금 회의시간 시작시간이 이전 회의의 끝 시간보다 크거나 같다면 가능.
#         if time_table[i][0] >= time_table[j][1]:
#             maxx = max(maxx, dp[j])
#     print(dp)
#     dp[i] = maxx + time_table[i][2]
        
# print(dp)
# print(dp[-1])