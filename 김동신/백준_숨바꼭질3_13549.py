#### dijkstra로 풀기

import heapq

def dijkstra(start):
    queue = [(start,0)]
    distance[start] = 0

    while queue:
        target, dist = heapq.heappop(queue)

        if dist > distance[target]:
            continue

        for i in graph[target]:
            if 0<=i[0]<=100000:
                cost = i[1]+dist
                if cost<distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue,(i[0],cost))

N,K = map(int,input().split())

distance = [1e9]*100001
graph = [[] for _ in range(100001)]
for i in range(100001):
    tmp = [(i-1,1),(i+1,1),(2*i,0)]
    graph[i] = tmp
dijkstra(N)
print(distance[K])

##### bfs로 풀기
import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
INF = int(1e9)
dp = [INF]*100001
dp[N] = 0


def bfs(start):
    queue = deque([start])

    while queue:
        now = queue.popleft()

        if 0<=now+1<=100000 and dp[now+1]>dp[now]+1:
            dp[now+1] = dp[now]+1
            queue.append(now+1)

        if 0<=now-1<=100000 and dp[now-1] > dp[now]+1:
            dp[now-1] = dp[now]+1
            queue.append(now-1)
        if 0<=now*2<=100000 and dp[now*2] > dp[now]:
            dp[now*2] = dp[now]
            queue.append(now*2)

bfs(N)
print(dp[K])
