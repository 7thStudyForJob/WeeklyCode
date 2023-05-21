import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)
dice = list(map(int, input().split()))  # 주사위의 입력값
piece = [0] * 4  # 현재 말의 위치
check = [False] * 34  # 윷놀이판 엔트리의 말 존재여부

arr = [i + 1 for i in range(21)] + [21] + [i + 1 for i in range(22, 27)] + [20, 29, 30, 25, 32, 25]
# 다음에 갈 위치 저장
score = [2 * i for i in range(21)] + [0, 13, 16, 19, 25, 30, 35, 28, 27, 26, 22, 24]  # 윷놀이판 엔트리의 점수
turn = [0] * 34  # 파란색 화살표가 있는 전환 지점
turn[5], turn[10], turn[15] = 22, 31, 28

ans = -sys.maxsize

def dfs(cnt, sum):
    global ans
    if cnt == 10:
        ans = max(ans, sum)
        return

    for i in range(4):
        prev = piece[i]
        cur = prev
        move = dice[cnt]

        if turn[cur] > 0:  # 파란색 화살표 지점 도달시 방향 전환
            cur = turn[cur]  # 현재 위치가 전환점인지 먼저 확인해서 방향 바꿔놓고, 이동 시작
            move = move - 1

        while move:
            cur = arr[cur]  # 남은 이동횟수만큼 칸 이동
            move = move - 1

        if cur != 21 and check[cur]:  # 도착위치가 아닌데, 해당 위치에 말이 있다면 못 놓음
            continue

        check[prev] = False
        check[cur] = True
        piece[i] = cur

        dfs(cnt + 1, sum + score[cur])  # 이동가능할 시, 해당 칸에 체크하고 점수추가해서 재귀 호출

        piece[i] = prev
        check[prev] = True
        check[cur] = False

dfs(0, 0)

print(ans)
