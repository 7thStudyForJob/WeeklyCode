import sys
import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue :
        dist, target = heapq.heappop(queue)

        if dist > distance[target] :
            continue
        else :
            for i in arr[target] :
                cost = dist + i[1]
                if cost < distance[i[0]] :
                    distance[i[0]] = cost
                    heapq.heappush(queue,(cost,i[0]))


input = sys.stdin.readline
INF = int(1e9)
N,M,K,X = map(int,input().split())

# (인덱스)번 노드에서 각 목적지까지의 거리
arr = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    a,b = map(int,input().split())
    # a에서 b로 가는 거리는 1
    arr[a].append((b,1))
# 출발점이 X일 때 각 노드까지의 최단 거리
dijkstra(X)

res = []

for i in range(1,N+1):
    # 만약 X로부터의 최단거리가 K인 노드가 있다면
    if distance[i] == K :
        # res에 넣기
        res.append(i)

# 문제에서 주어진대로 출력
if res :
    for j in res :
        print(j)
else :
    print(-1)