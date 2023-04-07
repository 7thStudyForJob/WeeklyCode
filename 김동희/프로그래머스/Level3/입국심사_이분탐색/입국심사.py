def solution(n, times):
    answer = float('inf')
    times.sort()
    start = times[0]
    end = times[-1] * n
    # 범위 : 시간
    # 기준 : 보좌관들이 전체시간 중 n 명이 되는 최소시간을 찾는 mid 값
    while start <= end:
        mid = (start + end) // 2
        peoples = 0
        for time in times:
            peoples += mid // time

        if peoples >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer