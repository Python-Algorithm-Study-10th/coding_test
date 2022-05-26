from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# bfs 풀이
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft() # 좌표를 기록하려면 
        #현 위치에서 네방향으로의 위치확인
        for i in range(4):
            nx=x+dx[i]  # 이동하면서 x 위치 확인
            ny=y+dy[i]  # 이동하면서 y 위치 확인
            
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
    return graph[n-1][m-1] # 마지막 도착한 오른쪽 아래 끝의 숫자 리턴
print(bfs(0,0))

# dfs 풀이
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return
    if graph[x][y]==1:
        graph[x][y]=graph[x][y]+1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    return graph[n-1][m-1]
print(dfs(0,0))   