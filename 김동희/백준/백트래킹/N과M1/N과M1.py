import sys; sys.stdin = open("N과M1.txt")
n, m = map(int, sys.stdin.readline().split())
result = [0] * m
permu = [False] * (n + 1)

def dfs(dept):
    if dept == m:
        print(*result)
        return

    for i in range(1, n+1):
        if not permu[i]:
            result[dept] = i
            permu[i] = True
            dfs(dept + 1)
            permu[i] = False

dfs(0)