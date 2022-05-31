from collections import deque
import sys

n,m,k,start=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)] # [ [](무시) [2,3] [3,4] [] []  ] 총 n+1개지만 처음 []은 무시하므로 n개
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
distance=[False for _ in range(n+1)] #만약 4일떄 [false(무시) false false false false] 0번노드부터 시작을 안하니 
                                    # 만약 n으로 하게되면 마지막노드를 표시할수없음.
                                    #distance는 0을 기준점으로 얼마나 떨어져있는지에대한 지표
# bfs풀이                            
def bfs():
    q=deque()
    q.append(start)           # 큐에는 기준이되는 좌표나 시작점을 넣는거!!
    distance[start]=0           # false 0 false false false  1번노드가 기준일떄 
    while q:
        now=q.popleft()         
        for next in graph[now]:   # 그래프에선 현위치를 기준으로 연결된 노드들을 나타내므로.
            if distance[next]==False: # False 라는것은 다른노드들은 아직 한번도 방문하지 않았으므로 
                distance[next]=distance[now]+1 # 방문하게되면 (방문한노드=현위치+1)이됨.
                q.append(next) # next를 큐에 추가하면 방문한곳을 기준으로 다시 그래프연결된 노드를 for문이 탐색

bfs() 

check=False
for i in range(len(graph)):
    if distance[i]==k: # 찾으려는값이 있으면
        print(i)  # 찾으려는값 노드출력
        check=True
if check==False: #찾으려는값 없으므로
    print(-1)


# dfs 풀이 
sys.setrecursionlimit(10**7) # 런타임에러나올떄 재귀의 최대깊이 제한 변경

distance[start]=0
def dfs(graph,start,distance):
    
    
    for next in graph[start]: # 2 3 
        if distance[next]==False:
            distance[next]=distance[start]+1
            
    for next in graph[start]: 
        dfs(graph,next,distance)

dfs(graph,start,distance)

check=False
for i in range(len(graph)):
    if distance[i]==k: # 찾으려는값이 있으면
        print(i)  # 찾으려는값 노드출력
        check=True
if check==False: #찾으려는값 없으므로
    print(-1)
