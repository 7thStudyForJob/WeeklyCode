import sys
sys.stdin=open("운동.txt")
input = sys.stdin.readline
# 모든 경로의 최소 합
V, E = map(int, input().split())
INF = float("inf")
arr = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a][b] = c

# k 경유지 (중간노드)
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# 출발지 = 도착지
answer = INF
for i in range(1, V+1):
    answer = min(answer, arr[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)
