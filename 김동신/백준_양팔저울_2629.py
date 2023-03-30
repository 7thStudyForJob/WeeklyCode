import sys

input = sys.stdin.readline

# 추의 정보
N = int(input())
weights = list(map(int, input().split()))
# 무거운 추부터 내림차순 정렬
weights.sort(reverse=True)

# 구슬의 정보
M = int(input())
marbles = list(map(int, input().split()))

# dp[i][j]는 i번째 추까지 확인했을 때, j무게인지 확인할 수 있는지를 의미
dp = [[0] * 40001 for _ in range(N)]
# 초기값 설정
dp[0][weights[0]] = 1

# 나머지 DP 배열 채워주기
for i in range(1, N):
    # 추에 대한 정보 받기
    weight = weights[i]
    # 우선 자기 자신의 무게는 측정 가능하므로 자기 자신을 나타내는 값 갱신
    dp[i][weight] = 1

    # 이전 단계에서 가능하다고 판단한 무게들 모두 받아오기
    for j in range(40001):
        if dp[i - 1][j] == 1:

            # 똑같이 받기
            dp[i][j] = 1

            # 해당 무게에서 자기 자신의 무게를 더하거나 뺀 무게도 가능하다고 표기
            if j - weight >= 0:
                dp[i][j - weight] = 1
            else:
                dp[i][weight - j] = 1

            if j + weight <= 40000:
                dp[i][j + weight] = 1

ans = []
# 구슬을 순회하면서 해당 구슬이 측정 가능한지 판단
for marble in marbles:
    if dp[-1][marble] == 1:
        ans.append("Y")
    else:
        ans.append("N")
print(*ans)