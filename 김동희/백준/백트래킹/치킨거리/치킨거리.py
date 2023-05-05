import sys
sys.stdin=open("치킨거리.txt")
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
citymat = [list(map(int, input().split())) for _ in range(n)]

# 치킨집 중에서 m 개만을 놓고 볼 때, => dfs 중복제거, 오름차순가지치기 가능
# 치킨거리의 최소값을 구하라. => 각 집에서 치킨집의 거리가 짧은 것들의 합을 result 갱신
info_houses = []
info_chicken = []
for r in range(n):
    for c in range(n):
        if citymat[r][c] == 1:
            info_houses.append((r, c))
        elif citymat[r][c] == 2:
            info_chicken.append((r, c))

select_chicken = [False] * len(info_chicken)
result = float("inf")
select = []

def dfs(k, start):
    global result
    if k == m:
        sum_v = 0
        for house in info_houses:
            min_distance = float("inf")
            for s in select:
                d = abs(house[0] - s[0]) + abs(house[1] - s[1])
                min_distance = min(min_distance, d)
            sum_v += min_distance
        result = min(result, sum_v)
        return

    for i in range(start, len(info_chicken)):
        if not select_chicken[i]:
            select_chicken[i] = True
            select.append(info_chicken[i])
            dfs(k + 1, i + 1)
            select.pop()
            select_chicken[i] = False

dfs(0, 0)
print(result)
