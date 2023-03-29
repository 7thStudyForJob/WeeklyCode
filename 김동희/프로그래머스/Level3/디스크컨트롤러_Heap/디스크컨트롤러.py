from heapq import heappush, heappop, heapify

# start, time
# 500 each
# start, time < 1000
# order by start ASC
# min => avg(times)

# min(평균) => time이 작은거 부터

def solution(jobs):
    heapify(jobs)
    n = len(jobs)
    waitroom = []
    time = total = 0
    while jobs or waitroom:
        while jobs and jobs[0][0] <= time:
            heappush(waitroom, [jobs[0][1], jobs[0][0]])
            heappop(jobs)
        if waitroom:
            time += waitroom[0][0]
            prior = heappop(waitroom)[1]
            total += time - prior
        else:
            time += 1

    answer = total // n
    return answer