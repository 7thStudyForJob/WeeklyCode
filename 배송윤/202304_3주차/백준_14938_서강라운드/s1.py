import sys
sys.stdin = open('input.txt')
INF = int(1e9)
n,m,r=map(int,input().split())
t=[0]+list(map(int,input().split()))
d=[[INF for _ in range(n+1)]for _ in range(n+1)]

def floid():
    # k = 거쳐가는 노드, i = 시작노드, j = 도착 노드
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                # i에서 j로 바로 가는 경우와, i에서 k를 거쳐 j로 가는 경우
                # 더 비용이 덜 드는 값으로 거리값 갱신
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])

# 거리표 초기화
for i in range(1,n+1):
    d[i][i]=0

# 간선 정보 입력
for _ in range(r):
    a,b,l=map(int,input().split())
    d[a][b]=l
    d[b][a]=l

# 함수 실행
floid()

ans=[0 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        # 수색 범위 보다 크면 스킵
        if d[i][j]>m:
            continue
        # i 번에서 시작하여 얻을 수 있는 아이템 누적
        ans[i]+=t[j]

# 최대값 출력
print(max(ans))