import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

graph=[]
for i in range(N):
    graph.append(list(map(int,input())))

def ice_dfs(x,y):
    # 주어진 범위를 벗어날 경우 false 리턴
    if x<0 or x>=N or y<0 or y>=M:
        return False  

    # 0인 지점이라면 그곳을 1로 하고 상하좌우에서도 동일한 작업을 재귀적으로 수행한다.
    if graph[x][y]==0:
        graph[x][y] = 1
        ice_dfs(x,y-1) # 좌
        ice_dfs(x,y+1) # 우
        ice_dfs(x-1,y) # 상
        ice_dfs(x+1,y) # 하
        return True

result=0

for i in range(N):
    for j in range(M):
        
        if ice_dfs(i,j):
            result+=1
            #상하좌우에서 동일한 작업을 재귀적으로 수행하기 때문에 여기서 1만 더해줘도 된다.
print(result)
