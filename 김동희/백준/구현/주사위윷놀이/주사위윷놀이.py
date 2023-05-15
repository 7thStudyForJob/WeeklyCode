import sys
sys.stdin = open("주사위윷놀이.txt")
sys.setrecursionlimit(1000)

class Node:
    def __init__(self, score, red, isBlue=None):
        self.score = score
        self.red = red
        self.isBlue = isBlue


def dfs(k):
    global horse_num, exist_check
    if k == 9:
        horse_num = [0] * 4
        exist_check = [False] * 43
        move(horse_num, exist_check)
        return
    # 4개의 말
    for i in range(4):
        check[k] = i
        dfs(k + 1)
        check[k] = -1

def move(horse_num, exist_check):
    global max_score
    score = 0
    # 스텝별로 몇번 말인지
    for i in range(10):
        end = horse_move(check[i], step[i], exist_check)
        if end == -1:
            return
        horse_num[check[i]] = end
        score += map_nodes[end].score
    max_score = max(max_score, score)


# 끝을 하나의 변수로 갱신하며 확인
def horse_move(horse, step, exist_check):
    temp = horse_num[horse]

    for i in range(step):
        # 말이 파란색 칸에서 이동을 시작하면
        if i == 0 and map_nodes[temp].isBlue:
            temp = map_nodes[temp].blue
            continue
        temp = map_nodes[temp].red
    # 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다
    if temp <= 40 and exist_check[temp]:
        return -1
    else:
        exist_check[horse_num[horse]] = False
        exist_check[temp] = True
        return temp



map_nodes = [Node(i, i + 2) if i % 2 == 0 else None for i in range(43)]

map_nodes[10].isBlue = map_nodes[20].isBlue = map_nodes[30].isBlue = True
map_nodes[10].blue = 11
map_nodes[20].blue = 17
map_nodes[30].blue = 31

map_nodes[11] = Node(13, 13)
map_nodes[13] = Node(16, 15)
map_nodes[15] = Node(19, 25)
map_nodes[17] = Node(22, 19)
map_nodes[19] = Node(24, 25)
map_nodes[25] = Node(25, 37)
map_nodes[31] = Node(28, 33)
map_nodes[33] = Node(27, 35)
map_nodes[35] = Node(26, 25)
map_nodes[37] = Node(30, 39)
map_nodes[39] = Node(35, 40)
map_nodes[42] = Node(0, 42)


Nodes = []
for i in range(43):
    if i % 2 == 0:
        Nodes.append([i, i + 2, False])
# 주사위
step = list(map(int, sys.stdin.readline().split()))

check = [0] * 10

# 말 번호
horse_num = [0] * 4

# 전역 변수로
exist_check = [False] * 43

max_score = 0
dfs(0)
print(max_score)

