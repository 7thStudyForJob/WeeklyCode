import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    now = heapq.heappop(scoville)
    while scoville:
        if now >= K:
            return answer

        new = heapq.heappop(scoville)
        mix_food = now + new * 2
        now = heapq.heappushpop(scoville, mix_food)
        answer += 1

    if now < K:
        answer = -1

    return answer