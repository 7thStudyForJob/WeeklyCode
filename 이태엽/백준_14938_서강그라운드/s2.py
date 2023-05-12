import sys
sys.stdin = open("input.txt", "r")
INF = int(1e9)
place, search, path = map(int, input().split())

item_lst = list(map(int, input().split()))
arr = [[INF] * place for _ in range(place)]
placeA_lst = []
placeB_lst = []
length_lst = []

for i in range(path):
    start, end, dist = map(int, input().split())
    arr[start-1][end-1] = min(arr[start-1][end-1], dist)
    arr[end-1][start-1] = min(arr[end-1][start-1], dist)
for i in range(place):
    arr[i][i] = 0
# for k in range(place):
#     for a in range(place):
#         for b in range(place):
#             arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
# k는 0  a는 1이라고 가정 b가 2이라고 가정
#     # placeA, placeB, length = map(int, input().split())
#     # placeA_lst.append(placeA)
#     # placeB_lst.append(placeB)
#     # length_lst.append(length)

# item_number_lst = []

# for i in range(1, place+1):
#     item_number = 0
#     item_number += item_lst[i-1]
#     for j in range(path):
#         if placeA_lst[j] == i and search >= length_lst[j]:
#             item_number += item_lst[placeB_lst[j]-1]
#         if placeB_lst[j] == i and search >= length_lst[j]:
#             item_number += item_lst[placeA_lst[j]-1]
#     item_number_lst.append(item_number)

print(arr)
