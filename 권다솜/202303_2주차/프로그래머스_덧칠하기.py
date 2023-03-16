def solution(n, m, section):
    answer = 0
    roller = 0
    for i in section:
        if i >= roller:
            roller = i + m
            answer += 1
    
    return answer