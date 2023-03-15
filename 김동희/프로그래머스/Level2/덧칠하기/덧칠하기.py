from collections import deque


def solution(n, m, section):
    answer = 0
    # section = deque(section)
    # n번까지 m개를 연속으로 칠하는데
    # section에 있는 것을 모두 칠해야 한다.
    # 최솟값을 구하라.
    # 1 5 29 45 // m = 4 44
    # 1. 수학 => section의 구간이 m이상일 경우 가장 많이 포함될 수 있도록 칠한다.
    # 정렬 후 첫값과 끝값을 나눈다?

    # start = section[0]
    # end = section[-1]
    # value = start
    # for i in range(start, end + 1, m):
    #     for j in range(i, i+m):
    #         if j in section:
    #             answer += 1
    #             print(j)
    #             break
    # print(answer)

    #     while end - start >= m:
    #         cnt = 0
    #         for i in range(start, start+m):
    #             if i in section:
    #                 section.popleft()

    #         start = section[0]
    #         answer += 1
    #     answer += 1

    # 1로
    arr = [0] * 100001
    for i in range(len(section)):
        arr[section[i]] = 1

    v = 0
    while v <= section[-1]:
        if arr[v] == 1:
            v += m
            answer += 1
        else:
            v += 1

    return answer

print(solution(8,4,[2,3,6]))
print(solution(5,4,[1,3]))
print(solution(4,1,[1,2,3,4]))
