def solution(n, m, section):
    answer = 0
    
    while section :
        idx = 0
        start = section.pop(0)
        end = start + m - 1
        answer+= 1
        for i in section:
            if end - i >= 0:
                idx += 1
            else:
                break
        section = section[idx:]
        
    
            
    return answer