import sys
sys.stdin = open("소수의연속합.txt")
N = int(input())
arr = []

def isSosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

check = [False, False] + [True] * (N-1)
def isSosu2(n):
    '''
    2배 부터 시작해서 자기만큼의 거리를 이미 check[n] = False
    '''
    for i in range(2 * n, N+1, n):
        check[i] = False

# 구해보기.
for i in range(2, N + 1):
    if check[i]:
        arr.append(i)
        isSosu2(i)

# 투포인터
answer = 0
start, end, sum = 0, 0, 0
M = len(arr)
while start < M:
    if sum > N or end == M:
        sum -= arr[start]
        start += 1
    else:
        sum += arr[end]
        end += 1
    if sum == N:
        answer += 1
print(answer)
