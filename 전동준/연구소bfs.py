import sys

n,m=map(int,sys.stdin.readline().split())

data=[] #초기맵리스트
# temp=[[0]*m for i in range(n)] # 벽을 설치한 뒤의 맵리스트 

temp=[]
for i in range(n):
    temp.append([0]*m)


for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=0
#dfs로 바이러스 퍼지기
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)
# 현재 맵에서 안전 영역 크기계산
def get_score(): # 이표현은 자주쓰는 방식
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score
#dfs로 울타리설치하면서 매번 안전영역크기계산
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result=max(result,get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1
dfs(0)
print(result)


from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=0

temp=[[0]*m for i in range(n)]


def bfs():
    global result
    q=deque()
    
    #바이러스 위치 찾기 
    for i in range(n):
        for j in range(m):
            temp[i][j]=graph[i][j]
            if temp[i][j]==2:
                q.append((i,j))
    #바이러스가 퍼뜨리기
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                q.append((nx,ny)) 
    # 0의 개수 (안전지대 개수) 카운트
    zero_score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                zero_score+=1
    # 0, zero_scroe=10(0의개수)
    result=max(result,zero_score)
    return result

# 벽을 설치하는 함수 구현
def wall(count):
    if count==3:
        bfs()
        return
    #벽을 설치하는 과정
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                count+=1
                wall(count)
                graph[i][j]=0
                count-=1
wall(0)
print(result)

    


    
        
        
