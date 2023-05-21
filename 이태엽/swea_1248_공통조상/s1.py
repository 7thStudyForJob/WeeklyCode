import sys
sys.stdin = open('input.txt')

def make_parent_list(lst):
    parent = [0] * V
    for i in lst:
        parent[i[1]-1] = i[0]
    return parent

def find_lca_and_subtree_size(v1, v2, parents):
    
    # 각 정점의 조상님들을 저장할 리스트
    ancestors1 = []
    ancestors2 = []
    
    # 루트까지 올라가며 각 정점의 조상을 추가
    while v1 != 1:
        ancestors1.append(v1)
        v1 = parents[v1-1]
        
    # 마지막에 루트를 추가
    ancestors1.append(1)
    
    while v2 != 1:
        ancestors2.append(v2)
        v2 = parents[v2-1]
    ancestors2.append(1)
    
    # 두 정점의 가장 가까운 공통 조상 찾기
    common = 0
    for ancestor in ancestors1:
        if ancestor in ancestors2:
            common = ancestor
            break
    
    # common을 루트로 하는 서브트리의 크기 구하기
    subtree_size = 1  # common 자신의 크기는 1로 초기화
    stack = [common]
    while stack:
        present_node = stack.pop()
        for idx, parents_node in enumerate(parents):
            if parents_node == present_node:
                stack.append(idx+1)
                subtree_size += 1
                
    return common, subtree_size

T = int(input())
for tc in range(1, T+1):
    
    V, E, first, second = map(int, input().split())
    arr = list(map(int, input().split()))
    
    new_arr = [(arr[i], arr[i+1]) for i in range(0, len(arr), 2)]
    
    tree = make_parent_list(new_arr)
    
    answer = find_lca_and_subtree_size(first, second, tree)
    # print(tree)
    print(f'#{tc} {answer[0]} {answer[1]}')
    