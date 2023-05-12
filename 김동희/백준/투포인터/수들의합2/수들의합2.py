import sys
sys.stdin = open("수들의합2.txt")
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
sum = 0
start_idx = 0
end_idx = 0
while start_idx < N:
    if sum > M or end_idx == N:
        sum -= arr[start_idx]
        start_idx += 1
    else:
        sum += arr[end_idx]
        end_idx += 1
    if sum == M:
        answer += 1
print(answer)
