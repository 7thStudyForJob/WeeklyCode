Fatigue = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
answer = float("inf")
picks_idx = {"diamond":0, "iron":1, "stone":2}

def DFS(idx, d, ir, s, minerals, p):
    global answer
    if idx >= len(minerals) or (not d and not ir and not s):
        answer = min(answer, p)
        return
    dp = ip = sp = 0
    for i in range(idx, min(idx+5, len(minerals))):
        dp += Fatigue[0][picks_idx[minerals[i]]]
        ip += Fatigue[1][picks_idx[minerals[i]]]
        sp += Fatigue[2][picks_idx[minerals[i]]]

    if d:
        DFS(idx + 5, d - 1, ir, s, minerals, p + dp)
    if ir:
        DFS(idx + 5, d, ir - 1, s, minerals, p + ip)
    if s:
        DFS(idx + 5, d, ir, s - 1, minerals, p + sp)

def solution(picks, minerals):
    # 곡괭이 선택 - 5번 연속 사용
    # 곡괭이 갯수 있음
    # 곡괭이가 없을 때까지 or 광물 없을 때 까지

    # 1. picks = 다이아, 철, 돌의 갯수를 확인
    # 2. minerals의 5개씩 한묶음으로 -> 다이아, 철, 돌의 갯수 확인 -> 숫자 리스트 -> 내림 정렬
    # 3. 정렬된 순서대로 다, 철, 돌 곡괭이 사용 - 피로도 갱신
    global answer
    DFS(0, picks[0], picks[1], picks[2], minerals, 0)
    return answer
