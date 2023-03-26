import sys
sys.stdin = open('input.txt')


def after_rotate(gears, gear, dir):
    global tmp_gears
    leftCur = gear
    leftCheck = gear - 1
    rightCur = gear
    rightCheck = gear + 1
    # gear의 좌우 상태 확인 후 돌린다.

    # 왼쪽 상태 확인
    tmp_dir = dir
    while leftCheck >= 0:
        
        # 극이 서로 다르다면, 왼쪽거를 현재 돌린 기어의 반대 방향으로 회전 
        if tmp_gears[leftCur][6] != tmp_gears[leftCheck][2]:
            rotate(gears, leftCheck, -tmp_dir)

        else:
            break
        leftCur -= 1
        leftCheck -= 1
        # ex) 2->1 번으로 넘어갈때, 2번이 돈 방향의 반대 방향으로 돌아야 하므로 방향 갱신 
        tmp_dir = -tmp_dir

    
    while rightCheck < 4:
        if tmp_gears[rightCur][2] != tmp_gears[rightCheck][6]:
            rotate(gears, rightCheck, -dir)
            dir = -dir
        else:
            break

        rightCur += 1
        rightCheck += 1


def rotate(gears, gear, dir):
    
    tmp = 0
    # 반시계
    if dir == -1:
        tmp = gears[gear][0]
        gears[gear] = gears[gear][1:]
        gears[gear].append(tmp)
        
    # 시계
    else:
        tmp = gears[gear][-1]
        gears[gear] = gears[gear][:-1]
        gears[gear].insert(0, tmp)
        
    return gears


gears = []
for _ in range(4):
    gears.append(list(input()))

R = int(input())

for i in range(R):
    gear, dir = map(int, input().split())
    gear -= 1
    # 이전 상태를 담을 리스트
    tmp_gears = gears[:]
    # print('돌리기전')
    # print(gears)
    after_rotate(gears, gear, dir)
    rotate(gears, gear, dir)
    # print('돌린후')
    # print(gears)

answer = 0
for i in range(4):
    answer += int(gears[i][0])*(2**i)
print(answer)
    