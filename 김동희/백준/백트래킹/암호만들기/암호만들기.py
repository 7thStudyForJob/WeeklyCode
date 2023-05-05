import sys
sys.stdin=open("암호만들기.txt")
sys.setrecursionlimit(1000)
input = sys.stdin.readline
L, C = map(int, input().split())
arr = list(input().split())

used = [False] * 15
alpha = ["a","e","i","o","u"]
result = []
arr.sort()

def dfs(k, cut):
    global result
    if k == L:
        a, b = 0, 0
        for i in range(L):
            if result[i] in alpha:
                a += 1
            else:
                b += 1

        if a >= 1 and b >= 2:
            print(*result, sep="")
        return

    for i in range(cut, C):
        if not used[i]:
            used[i] = True
            result.append(arr[i])
            dfs(k + 1, i + 1)
            result.pop()
            used[i] = False

dfs(0, 0)