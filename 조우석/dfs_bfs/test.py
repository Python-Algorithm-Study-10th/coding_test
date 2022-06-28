from collections import deque
from math import dist
import sys
#도시개수,도로의개수,거리정보,출발도시번호
n,m,k,start=map(int,sys.stdin.readline().split())
graph=[]

# 모든 도로 정보 입력받기
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph.append([a,b])
    
#모든 도시에 최단 거리 초기화
distance=[-1]*(n+1) 
distance[start]=0
visited=[False] * n
# distance[start]=0
def dfs(graph,start,distance):
    
    #현재 도시 이동할수 있는 모든 도시 확인
    for next_n in graph[start]:
        #아직 방문안한 도시
        if not visited[next_n]:
            
            if distance[next_n]==-1:
                #최단 거리 갱신
                distance[next_n]=distance[start]+1
                dfs(graph,next_n,distance)
    #최단 거리 k인 모든 도시 번호를 오름차순 출력
    check=False
    for i in range(1,n+1): # distance에서 k인 노드찾기(오름차순이라서 1~n)
        if distance[i]==k:
            print(i)
            check=True
    #최단 거리 k인 도시 없으면 -1
    if check==False:
        print(-1)        

dfs(graph,start,distance)
