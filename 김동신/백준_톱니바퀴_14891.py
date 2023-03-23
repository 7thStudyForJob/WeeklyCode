import sys
from collections import deque

input = sys.stdin.readline


# 하나의 톱니바퀴를 시계방향으로 회전
def rotate_right(gear_arr):
    last = gear_arr.pop()
    gear_arr.appendleft(last)
    return gear_arr


# [0,0,0,0,0,1,1,0]을 [0,0,0,0,0,0,1,1]로 만들 수 있음


# 하나의 톱니바퀴를 반시계방향으로 회전
def rotate_left(gear_arr):
    last = gear_arr.popleft()
    gear_arr.append(last)
    return gear_arr


# [0,0,0,0,0,1,1,0]을 [0,0,0,1,1,0,0,0]로 변경

# 관련된 전체 톱니바퀴 회전 (톱니바퀴 번호, 방향)
def rotate_gear(num, d):
    # 방문처리 (이미 돌린 톱니바퀴를 또 다시 돌리지 않도록)
    visited[num] = 1

    # 지금 돌리는 톱니바퀴의 왼쪽 톱니바퀴와 극 비교
    # 왼쪽 톱니바퀴의 2번 톱니와 지금 톱니바퀴의 6번 톱니 비교
    if num - 1 >= 0 and visited[num - 1] == 0 and gears[num - 1][2] != gears[num][6]:
        # 해당 톱니바퀴를 중심으로 다시 재귀함수 호출
        rotate_gear(num - 1, -d)

    # 지금 돌리는 톱니바퀴의 오른쪽 톱니바퀴와 극 비교
    if num + 1 < 4 and visited[num + 1] == 0 and gears[num + 1][6] != gears[num][2]:
        rotate_gear(num + 1, -d)

    # 방향에 따라 회전시키기
    if d == 1:
        # 회전한 결과값을 톱니바퀴의 위치에 덮어씌우기
        gears[num] = rotate_right(gears[num])
    else:
        gears[num] = rotate_left(gears[num])


# popleft, appendleft를 사용하기 위해 deque로 설정
gears = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

K = int(input())
for _ in range(K):
    # 한번 회전시킬 때마다 방문배열 초기화
    visited = [0, 0, 0, 0]
    target, delta = map(int, input().split())
    # 회전 로직 실행
    rotate_gear(target - 1, delta)

score = 0
# 회전 한 후에 점수 계산
for g in range(4):
    top_of_gear = gears[g][0]
    # 만약, 12시 톱니가 S극이라면
    if top_of_gear == 1:
        # 점수 추가
        score += 2 ** g

print(score)