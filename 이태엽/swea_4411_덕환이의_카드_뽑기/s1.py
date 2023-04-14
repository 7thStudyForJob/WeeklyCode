import sys
sys.stdin = open("sample_input.txt", "r")

sys.setrecursionlimit(99999999)
def josephus(n, k):
  ans = 1  
  for i in range(1, n):
    ans = (ans+k)%(i+1) + 1
  return ans
# def josephus(n, circulation):
#   if n == 1:
#     return 1
#   return (josephus(n-1, circulation) + circulation) % n + 1

T = int(input())
for test_case in range(1, T + 1):
  n, k = map(int, input().split())
#   circulation = k % n
#   print(josephus(n, circulation))
  ans = 1
  for i in range(1, n):
    ans = (ans+k)%(i+1) + 1
  print('#{0} {1}'.format(test_case, ans))