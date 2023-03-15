
def solution(n, m , section):
    answer = 0					
    while section:
        start = section.pop(0)
        while section and start + m > section[0]: 
            section.pop(0)
        answer += 1
    return answer