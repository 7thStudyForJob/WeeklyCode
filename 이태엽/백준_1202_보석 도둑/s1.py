import sys
import heapq

sys.stdin = open('input.txt')

n,k = map(int,input().split())
jews= [list(map(int,input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jews.sort()
bags.sort()

answer = 0
tmp_lst = [] 
 
for bag in bags:
    while jews and jews[0][0] <= bag:
        heapq.heappush(tmp_lst, -jews[0][1])
        heapq.heappop(jews)
    if tmp_lst:
        answer -= heapq.heappop(tmp_lst)
print(answer)