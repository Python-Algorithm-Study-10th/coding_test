from sys import stdin

n,m = map(int,stdin.readline().split())

data=[] #초기맵리스트

graph =[]
for i in range(n):
    graph.append([0]*m)


for i in range(n):
    data.append(list(graph(int,stdin.readline().split())))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=0
#바이러스 확산 범위 계산 함수
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                virus(nx,ny)
#안전 영역 크기(개수) 계산
def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                score += 1
    return score

#dfs로 울타리설치하면서 매번 안전영역크기계산
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                graph[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if graph [i][j] == 2:
                    virus(i,j)
        result=max(result,get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count+=1
                dfs(count)
                data[i][j] = 0
                count -= 1
dfs(0)
print(result)