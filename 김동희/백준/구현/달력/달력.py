import sys
sys.stdin = open("달력.txt")

input = sys.stdin.readline
count = [0]*367

N = int(input())
Start = 0
End = 0
for _ in range(N):
    S, E = map(int, input().split())
    for i in range(S, E+1):
        count[i] += 1
    Start = min(Start, S)
    End = max(End, E)

answer = 0
r = 0
c = 0
for i in range(Start, End + 2):
    if count[i] != 0:
        r += 1
        c = max(c, count[i])
    elif count[i] == 0:
        answer += r * c
        r = 0
        c = 0
print(answer)


