N = int(input())
arr = list(map(int, input().split()))
arr.sort()

X = int(input())

start = 0
end = N-1
cnt = 0
while start < end:
    tmp = arr[start] + arr[end]
    if tmp > X:
        end -= 1
    elif tmp == X:
        cnt += 1
        end-=1
    else:
        start += 1
print(cnt)