def solution(n, info):
    global max_gap, ans
    # 어피치 점수 계산
    # 나중에 라이언 점수가 오를 때마다, 그만큼 빼주기
    # 즉, 지금은 어피치가 얻을 수 있는 최대 점수
    apeach_score = 0
    for i in range(len(info)):
        if info[i]:
            apeach_score += (10 - i)

    # 어피치와 라이언의 점수 차
    max_gap = 0

    # 점수 차가 가장 클 때의 라이언 사격 기록
    ans = []

    # k: 점수, arrows: 남은 화살, target: 라이언의 사격 기록
    def dfs(k, arrows, ryan_score, apeach_score, target):
        global max_gap, ans
        
        # 화살이 다 떨어졌거나, 0점까지 다 쏜 경우
        if arrows <= 0 or k == -1:
            # 라이언이 이긴 경우
            if ryan_score > apeach_score:
                # 라이언이 이미 이겼는데 화살이 남은 경우
                # 가장 뒷쪽에서부터 채우기(정답 조건)
                i = 10
                while arrows:
                    if target[i] < n:
                        target[i] += 1
                        arrows -= 1
                    else:
                        i -= 1
                
                # 라이언과 어피치의 점수차
                gap = ryan_score - apeach_score
                # 만약, 기존 최대차와 같다면 배열에 추가
                if gap == max_gap:
                    ans.append(target[::-1])
                # 최대차가 더 높다면 새로 할당해주고, max_gap값 갱신
                elif gap > max_gap:
                    ans = [target[::-1]]
                    max_gap = gap
            return
        
        # 각 점수에서 이긴다,진다 로 나눠서 dfs 재귀 호출
        # k점에서 이길 경우(이기려면 남은 화살이 어피치가 쏜 개수보다 많아야함)
        if arrows > info[10 - k]:
            # 라이언이 쏜 화살 개수 기록 (어피치보다 딱 한개만 더 쏘기)
            target[10 - k] = info[10 - k] + 1
            # 어피치가 0발을 쏜 경우 어피치 점수에는 변화 없음
            new_apeach_score = apeach_score
            # but, 어피치가 쏜 경우, 맨 처음에 점수를 추가해줬으므로 그만큼 빼주기
            if info[10 - k] != 0:
                new_apeach_score = apeach_score - k
            # 각 값들을 갱신하여 재귀호출
            dfs(k - 1, arrows - (info[10 - k] + 1), ryan_score + k, new_apeach_score, target[:])

        # k점에서 질 경우
        # 라이언은 0발을 쏘도록 하기
        target[10 - k] = 0
        # 나머지는 그대로 해서 재귀호출
        dfs(k - 1, arrows, ryan_score, apeach_score, target[:])


    targets = [0] * 11
    dfs(10, n, 0, apeach_score, targets)
    # ans에는 최대차로 만들 수 있는 사격 기록들이 있음
    if ans:
        # 배열을 정렬하면, 가장 낮은 점수를 기준으로 정렬 (ans배열에 넣을 때 역정렬로 넣었기 때문)
        ans.sort()
        # 가장 낮은 점수가 가장 높은 배열을 다시 역정렬해서 반환
        return ans[-1][::-1]
    else:
        # 만약 ans 배열이 비어있다면, 라이언이 이길 수 없다는 뜻이므로 -1 반환
        return [-1]