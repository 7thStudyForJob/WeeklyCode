import sys
sys.stdin = open('input.txt')

n = int(input())
canlender = [0] * 366

for _ in range(n):
    start, end = map(int, input().split(' '))
    for i in range(start, end + 1):
        canlender[i] += 1

row = 0
col = 0
result = 0
for i in range(366):
    if canlender[i] != 0:
        row = max(row, canlender[i])
        col += 1
    else:
        result += row * col
        row = 0
        col = 0
result += row * col
print(result)