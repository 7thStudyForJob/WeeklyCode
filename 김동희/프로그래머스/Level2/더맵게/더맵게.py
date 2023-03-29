from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1: return -1
        i = heappop(scoville)
        j = heappop(scoville)
        x = i + (j * 2)
        heappush(scoville, x)
        answer += 1
    return answer