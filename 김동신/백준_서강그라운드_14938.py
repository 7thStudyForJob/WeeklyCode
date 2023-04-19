##### 다익스트라
import heapq
N,M,R = map(int,input().split())
items = list(map(int,input().split()))

edges = [[] for _ in range(N+1)]
for _ in range(R):
    a,b,c = map(int,input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))

INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance = [INF]*(N+1)
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if dist>distance[now]:
            continue

        for edge in edges[now]:
            cost = dist+edge[1]
            if cost<distance[edge[0]]:
                distance[edge[0]] = cost
                heapq.heappush(queue,(cost,edge[0]))
    return distance

ans = 0
for i in range(1,N+1):
    res = dijkstra(i)
    score = 0
    for j in range(1,N+1):
        if res[j]<=M:
            score+=items[j-1]
    if score>ans:
        ans = score

print(ans)


####### 플로이드 워셜
import heapq

N,M,R = map(int,input().split())
items = list(map(int,input().split()))

INF = int(1e9)
distance = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            distance[i][j] = 0

edges = [[] for _ in range(N+1)]
for _ in range(R):
    a,b,c = map(int,input().split())
    distance[a][b] = c
    distance[b][a] = c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])

ans = 0
for i in range(1,N+1):
    score = 0
    for j in range(1,N+1):
        if distance[i][j]<=M:
            score+=items[j-1]
    if ans<score:
        ans = score
print(ans)
