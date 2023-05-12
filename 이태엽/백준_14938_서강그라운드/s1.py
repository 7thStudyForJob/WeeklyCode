import sys
sys.stdin = open("input.txt", "r")

place, search, path = map(int, input().split())

item = str(input())

item = item.replace(" ", "")
item_lst = []

for i in item:
    item_lst.append(i)
item_lst = list(map(int, item_lst))

placeA_lst = []
placeB_lst = []
length_lst = []

for i in range(path):
    placeA, placeB, length = map(int, input().split())
    placeA_lst.append(placeA)
    placeB_lst.append(placeB)
    length_lst.append(length)

item_number_lst = []
# 각 지역에 떨어질 경우 모두 계산
for i in range(1, place+1):
    item_number = 0
    # 일단 떨어진 지역 아이템을 챙긴다.
    item_number += item_lst[i-1]
    # 각 원소의 인덱스 J와 값 placeA_place 동시에 반환하는 enumerate
    for j, placeA_place in enumerate(placeA_lst):
        # 만약 placeA_lst의 값이 떨어진 지역과 같다면
        if placeA_place == i:
            # 떨어진 지역이 placeA_lst에서 가지는 인덱스를 length_lst의 인덱스에 대입해서, 추적 범위 안이라면
            # placeB_lst의 그 인덱스에서 나오는 지역번호에 있는 아이템도 챙긴다.
            if search >= length_lst[j]:
                item_number += item_lst[placeB_lst[j]-1]
    # 반대 과정도 수행한다.
    for j, placeB_place in enumerate(placeB_lst):
        if placeB_place == i:
            if search >= length_lst[j]:
                item_number += item_lst[placeA_lst[j]-1]
    item_number_lst.append(item_number)
print(item_number_lst)

