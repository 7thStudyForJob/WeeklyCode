import sys; sys.stdin=open("서강그라운드.txt")
import heapq

n, m, r = map(int, input().split())

node = [[] for _ in range(n+1)]
item = [0] + list(map(int, input().split()))

INF = float("inf")

for i in range(r):
    a, b, l = map(int, input().split())
    node[a].append((b, l))
    node[b].append((a, l))
# print(node)

def Dij(k):
    value = [INF] * (n+1)
    value[k] = 0

    pq = []
    heapq.heappush(pq, (0, k))

    while pq:
        x, U = heapq.heappop(pq)

        for V, W in node[U]:
            if x+W < value[V]:
                value[V] = x+W
                heapq.heappush(pq, (x+W, V))
        # print(pq)
        # print('value : ',value)

    sum = 0
    for i in range(1, n+1):
        if value[i] <= m:
            sum += item[i]

    return sum

ans = 0
for i in range(1, n+1):
    ans = max(ans, Dij(i))

print(ans)
