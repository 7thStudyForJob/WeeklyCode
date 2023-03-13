import sys; sys.stdin=open("분해합.txt")

N = int(input())

# N의 분해합이 M이라면
# N은 M의 생성자
# N의 생성자 중에 가장 작은 값은?

# x의 분해합이 N인 경우의 모든 x중 가장 작은 값
#N = x + x[모든자릿수]
# N = 216
answer = 0
ans_list = []
for i in range(1, N+1):

    num = sum(map(int, str(i)))
    num_sum = num + i

    if num_sum == N:
        ans_list.append(i)
print(ans_list[0])









