import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
origin_arr = list(map(int,input().split()))
arr = sorted(set(origin_arr))

for a in origin_arr:
    print(bisect_left(arr,a),end=' ')