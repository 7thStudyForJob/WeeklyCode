from heapq import heappop, heappush, heapify
import sys
sys.stdin = open("보석도둑.txt")

n, k = map(int, sys.stdin.readline().split())
dia = []
for _ in range(n):
    d = list(map(int, sys.stdin.readline().split()))
    heappush(dia, d)
bag = []
for _ in range(k):
    c = int(sys.stdin.readline())
    bag.append(c)
bag.sort()

answer = 0
Q = []
# 최소 담을수 있는 가방부터 dia목록 빼놓고 heapq로 최대가격 pop and push -> pop
for b in bag:
    while (dia and b >= dia[0][0]):
        heappush(Q, -heappop(dia)[1])
    if Q:
        answer -= heappop(Q)

print(answer)



