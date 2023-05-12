import sys
sys.stdin = open('input.txt')


def find_lca_and_subtree_size(v1, v2, parents):
    # 각 정점의 조상을 저장할 set

    ancestors1 = []
    ancestors2 = []
    
    # 루트까지 올라가며 각 정점의 조상을 추가
    while v1 != 1:
        ancestors1.append(v1)
        v1 = parents[v1-1]
    ancestors1.append(1)
    while v2 != 1:
        ancestors2.append(v2)
        v2 = parents[v2-1]
    ancestors2.append(1)
    # 두 정점의 가장 가까운 공통 조상 찾기
    lca = None
    for ancestor in ancestors1:
        if ancestor in ancestors2:
            lca = ancestor
            break
    
    # lca를 루트로 하는 서브트리의 크기 구하기
    subtree_size = 1  # 루트 노드 자신의 크기는 1로 초기화
    stack = [lca]
    while stack:
        node = stack.pop()
        for idx, parents_node in enumerate(parents):
            if parents_node == node:
                stack.append(idx+1)
                subtree_size += 1
                
    return lca, subtree_size

T = int(input())
for tc in range(T):
    V, E, first, second = map(int, input().split())
    arr = list(map(int, input().split()))
    new_arr = [(arr[i], arr[i+1]) for i in range(0, len(arr), 2)]
    def make_parent_list(edges):
        # 루트 노드의 부모 노드 번호는 0으로 표현합니다.
        parent = [0] * (V + 1)
        for edge in edges:
            parent[edge[1]] = edge[0]
        return parent
    tree = make_parent_list(new_arr)[1:]
    find_lca_and_subtree_size(first, second, tree)
    print(f'#{tc} {find_lca_and_subtree_size(first, second, tree)[0]} {find_lca_and_subtree_size(first, second, tree)[1]}')
    