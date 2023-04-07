import sys
input = sys.stdin.readline

N = int(input())

nodes = set()
end_times = {}
for _ in range(N):
    a,b,c = map(int,input().split())
    nodes.add(a)
    nodes.add(b)
    if b not in end_times.keys() or end_times[b][1]<c:
        end_times[b] = (a,c)

nodes = sorted(list(nodes))
length = len(nodes)
dp = [0] * (length)

link = {}
for i in range(length):
    link[nodes[i]] = i

# nodes에는 시작시간과 끝나는 시간이 모두
# end_times에는 끝나는 시간만

for node in nodes:
    if node in end_times.keys():
        dp[link[node]] = max(dp[link[end_times[node][0]]]+end_times[node][1], dp[link[node]-1])
    else:
        dp[link[node]] = dp[link[node]-1]
print(dp[-1])