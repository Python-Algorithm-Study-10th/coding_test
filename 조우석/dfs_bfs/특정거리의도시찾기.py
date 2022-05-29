from collections import deque
from math import dist
import sys
#도시개수,도개,거리정보,출발도시번호
n,m,k,x=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
# 모든 도로 정보 입력받기
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
#모든 도시에 최단 거리 초기화
distance=[-1]*(n+1)
distance[x]=0

q=deque([x])
while q:
    now=q.popleft()
    #현재 도시 이동할수 있는 모든 도시 확인
    for next_node in graph[now]:
        #아직 방문안한 도시
        if distance[next_node]==-1:
            #최단 거리 갱신
            distance[next_node]=distance[now]+1
            q.append(next_node)
#최단 거리 k인 모든 도시 번호를 오름차순 출력
check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True
#최단 거리 k인 도시 없으면 -1
if check==False:
    print(-1)