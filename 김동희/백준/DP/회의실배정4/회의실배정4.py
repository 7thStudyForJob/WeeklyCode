import sys; sys.stdin = open("회의실배정4.txt")

n = int(input())
meets = [-1] * n

for i in range(n):
    s, e, p = map(int, input().split())
    meets[i] = (s, e, p)

# 종료시간이 빠른 순서와 함께 시작시간이 빠른 순서대로
meets.sort(key=lambda m: (m[1], m[0]))

dp = [0] * n
dp[0] = meets[0][2]

for i in range(1, n):
    t = 0
    for j in range(i):
        if meets[j][1] <= meets[i][0]:
            t = j

    if t > 0:
        dp[i] = max(dp[i-1], dp[t] + meets[i][2])
    else:
        dp[i] = max(dp[i-1], meets[i][2])

print(dp[n-1])