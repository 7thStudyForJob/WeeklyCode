import sys
sys.stdin = open('input.txt')

C, N = map(int, input().split())
cost_list = [list(map(int, input().split())) for _ in range(N)]
dp = [1e7 for _ in range(C + 100)]
dp[0] = 0

for cost, num_people in cost_list:
    # num_people 이후로 반복문을 돌리며 최소값 갱신
    for i in range(num_people, C + 100):
        # (i - num_people)명의 값에 현재 cost 더한 값과, 현재 i명의 값을 비교해 최소값으로 갱신
        # ex) 12명(i=12) 일때, num_people이 3이라면,
        # 9명일 때 최소 비용값에 cost를 더한 값(9+3=12)과 가장 최근에 갱신된 12명일 때 비용을 비교한다.
        dp[i] = min(dp[i - num_people] + cost, dp[i])

# print(dp)
# C명 이후로 최소값을 확인해야 한다.
#
print(min(dp[C:]))