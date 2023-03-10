import sys
input = sys.stdin.readline

N,K = map(int,input().split())
visited = [0]*N
arr = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i!=j:
                arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])

res = 100000000000

def recursion_test(start,visit,dist):
    global res
    if sum(visit) == N:
        if dist<res:
            res = dist
        return

    for t in range(N):
        if visit[t] == 0:
            next = arr[start][t]
            if dist+next > res:
                continue
            else:
                visit[t] = 1
                recursion_test(t,visit,dist+next)
                visit[t] = 0

visited[K] = 1
recursion_test(K,visited,0)
print(res)
