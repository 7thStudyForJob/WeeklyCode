import sys
sys.stdin = open("주사위윷놀이.txt")
sys.setrecursionlimit(1000)

class Node:
    def __init__(self, n, next, isBlue = None, blue = None):
        self.n = n
        self.next = next
        self.isBlue = isBlue
        self.blue = blue


def dfs(k):
    global horse_num, exist_check
    if k == 9:
        # 모두 뽑혔을 때, 이동을 계산을 해야하므로 초깃값.
        horse_num = [0] * 4
        exist_check = [False] * 43
        move(horse_num, exist_check)
        return

    for i in range(4):
        select[k] = i
        dfs(k + 1)

def move(horse_num, exist_check):
    global max_score
    score = 0
    # 모두 이동했을 때 마지막이 조건에 맞는지 확인
    # 변수 갱신
    for i in range(10):
        end = horse_move(select[i], step[i], exist_check)
        if end == -1:
            return
        horse_num[select[i]] = end
        score += map_node[end].n
    max_score = max(max_score, score)

def horse_move(horse, step, exist_check):
    node = horse_num[horse]
    # 스텝별로도 움직여 주면서
    for i in range(step):
        # 시작이면서 블루면 블루로 노드 변경
        if i == 0 and map_node[node].isBlue:
            node = map_node[node].blue
            continue
        node = map_node[node].next

    if node < 41 and exist_check[node]:
        return -1
    else:
        exist_check[node] = True
        # 처음 자리수를 다시 False
        exist_check[horse_num[horse]] = False
        return node



map_node = [] # new Node[]

for i in range(43):
    if i % 2 == 0:
        map_node.append(Node(i, i+2))
    else:
        map_node.append(None)

map_node[10].isBlue = True
map_node[20].isBlue = True
map_node[30].isBlue = True
map_node[10].blue = 11
map_node[20].blue = 17
map_node[30].blue = 31

# 13, 16, 19 => 11, 13, 15
map_node[11] = Node(13, 13)
map_node[13] = Node(16, 15)
map_node[15] = Node(19, 25)

# 22, 24 => 17, 19
map_node[17] = Node(22, 19)
map_node[19] = Node(24, 25)

# 25
map_node[25] = Node(25, 37)

# 31, 33, 35 => 28, 27 ,26
map_node[31] = Node(28, 33)
map_node[33] = Node(27, 35)
map_node[35] = Node(26, 25)

# 37, 39 => 30, 35
map_node[37] = Node(30, 39)
map_node[39] = Node(35, 40)

# 42 => 0
map_node[42] = Node(0, 42)
#주사위 한 면
step = list(map(int, sys.stdin.readline().split()))
# 총 10개를 뽑아
select = [0] * 10
# 4개 중에서
horse_num = [0] * 4
# 이미 놓은 말인지 체크
exist_check = [False] * 43
# 최댓값
max_score = 0
dfs(0)
print(max_score)




