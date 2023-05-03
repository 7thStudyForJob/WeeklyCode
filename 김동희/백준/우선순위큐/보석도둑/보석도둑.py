from heapq import heappop, heappush, heapify
import sys
sys.stdin = open("보석도둑.txt")

n, k = map(int, sys.stdin.readline().split())
dia = []
for _ in range(n):
    d = list(map(int, sys.stdin.readline().split()))
    heappush(dia, d) # 무게가 적은거 부터.

bag = []
for _ in range(k):
    c = int(sys.stdin.readline())
    bag.append(c)
bag.sort() # 오름차순. 담을 수 있는 무게가 적은 것 부터

answer = 0
Q = []
# 최소 담을수 있는 가방부터 dia목록 빼놓고 heapq로 최대가격 pop and push -> pop
for b in bag: #1 2 34
    while (dia and b >= dia[0][0]):
        heappush(Q, -heappop(dia)[1]) # -10, -20 가격만 => 최소값으로 먼저 들어가는데 , - heapq a -b b - a
    if Q: # 그 가방에 넣을보석이 있다면
        answer -= heappop(Q) #가격 0 -20 가격은 0보다 큼.

print(answer)



