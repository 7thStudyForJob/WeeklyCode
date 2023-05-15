import sys
sys.stdin=open("N과M2.txt")
sys.setrecursionlimit(5000)

n, m = map(int, sys.stdin.readline().split())

result = [0] * m
permu = [False] * (n + 1)

def dfs(dept, cut):
    if dept == m:
        print(*result)
        return

    for i in range(1, n+1):
        if not permu[i] and cut < i:
            permu[i] = True
            result[dept] = i
            dfs(dept + 1, i)
            permu[i] = False

dfs(0, 0)