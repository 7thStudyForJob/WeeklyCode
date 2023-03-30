import sys
sys.stdin = open('input.txt')

from collections import deque
L, S = map(int, input().split())
next = [0] * (101)
visited = [False] * (101)
dist = [0] * 101

def bfs(start):
    visited[start] = False
    q = deque()
    q.append(start)
    
    while q:
        
        cur = q.popleft()
        if cur == 100:
            break
        # 현재 위치에서 주사위를 굴린다.
        for i in range(1, 7):
            new = cur + i
            # 이동 한 값이 100을 넘어가면 다시 굴린다.
            if new > 100: 
                continue

            # 사다리 또는 뱀이라면 바로 순간이동
            new = next[new]
            # new 칸이 방문하지 않았다면
            if dist[new] == 0:
                # 해당 칸을 다음 이동할 칸에 넣는다.
                q.append(new)
                # new는 현재 칸에 +1 누적하여 거리를 갱신
                dist[new] = dist[cur] + 1 
    

# 사다리 정보 입력
for _ in range(L):
    s, e = map(int, input().split())
    next[s] = e

# 뱀 정보 입력
for _ in range(S):
    s, e = map(int, input().split())
    next[s] = e

# next에 각자의 칸 번호 입력
for i in range(101):
    if next[i] == 0:
        next[i] = i

# 보드 현황
print(next)

bfs(1)
print(dist)


print(dist[-1])
