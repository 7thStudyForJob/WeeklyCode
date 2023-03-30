import heapq

def solution(scoville, K):
    answer = 0
    keep_going = True
    
    heapq.heapify(scoville)
    print(scoville)
    if scoville[0] >= K:
        return answer
    
    
    while scoville[0] < K:
        print(scoville)
        if len(scoville) == 1:
            answer = -1
            return answer
        
        
    
        else:            
            print('a빼기전', scoville)
            a = heapq.heappop(scoville)
            print('a뺀후', scoville)
            b = heapq.heappop(scoville)
            print('b뺀후', scoville)
            new = a + (b * 2)
            heapq.heappush(scoville, new)
            answer += 1
        
       
        
            
    
    return answer