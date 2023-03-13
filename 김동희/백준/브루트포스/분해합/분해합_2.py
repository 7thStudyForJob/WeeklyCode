import sys; sys.stdin=open("분해합.txt")
n = int(input())
n_length = len(str(n))
new_n = n - (n_length * 9)

answer = 0
for i in range(new_n, n+1):
    sum = i
    k = i
    while k > 0:
        sum += (k % 10)
        k //= 10
    if sum == n:
        answer = i
        break
print(answer)