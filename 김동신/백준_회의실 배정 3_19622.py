import sys

input = sys.stdin.readline

N = int(input())
# dp[i]는 i번째 회의까지 배정받았을 때 최대 인원
dp = [0] * N

for i in range(N):
    s, e, people = map(int, input().split())

    # 초기에는 그냥 할당
    if i < 2:
        dp[i] = people
    # 3번째 회의부터는 두번째 전 회의와 3번째 전 회의 중 큰 값에 현재 회의 인원 더해주기
    # 왜냐하면, 바로 직전이나 직후 회의는 회의시간이 무조건 겹치기 때문
    else:
        dp[i] = max(dp[i - 2], dp[i - 3]) + people
# dp 에는 각 회의까지 받았을 때의 최대 인원이 나오게됨
# 따라서, dp배열에서 가장 큰 값이 가장 많이 받을 수 있는 인원
ans = max(dp)
print(ans)