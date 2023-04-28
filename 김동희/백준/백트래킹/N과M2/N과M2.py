import sys; sys.stdin=open("N과M2.txt")
n, m = map(int, sys.stdin.readline().split())

result = [0] * m
check = [False] *(n+1)

def dfs(dept, cut):
    if dept == m:
        print(*result)
        return

    for i in range(1, n+1):
        if not check[i] and cut < i:
            check[i] = True
            result[dept] = i
            dfs(dept + 1, i)
            check[i] = False

dfs(0, 0)