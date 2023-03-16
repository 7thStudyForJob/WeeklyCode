from itertools import product

def solution(users, emoticons):
    # 결과
    answer = [-1,-1]
    
    # 할인율 조합 생성
    discountArr = list(product([10,20,30,40],repeat=len(emoticons)))
    
    for discount in discountArr:
        serviceUser = 0
        revenue = 0
        
        # 사용자별 해당 할인율 조합에서의 이모티콘 구매 혹은 서비스 가입 여부 판별
        for user in users:
            emoCost = 0
            
            for i in range(len(emoticons)):
                # 이모티콘의 할인율이 사용자가 정한 할인 비율보다 클 경우 구매한다.
                if discount[i] >= user[0]:
                    emoCost += emoticons[i] * (100-discount[i])/100
            
            # 이모티콘을 구매한 금액이 사용자가 정한 금액보다 클 경우 서비스 가입
            if emoCost >= user[1]:
                serviceUser += 1
            else:
                revenue += emoCost
        
        # 기존보다 서비스 가입자가 큰 경우
        if answer[0] < serviceUser:
            answer[0] = serviceUser
            answer[1] = revenue
        # 기존과 서비스 가입자 수가 같은 경우
        elif answer[0] == serviceUser:
            answer[1] = max(answer[1],revenue)
            
    return answer