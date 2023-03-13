import sys; sys.stdin=open("블랙잭.txt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)
answer = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                answer = max(answer, arr[i] + arr[j] + arr[k])
print(answer)