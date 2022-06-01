import sys
from collections import deque
N,M,K,X= map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
print(graph)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
#[[],[2,3][3,4],[],[]] 과 같이 생성
distance=[-1]*(N+1) #모든 거리에 대한 최단거리 초기화
distance[X]=0 #출발 도시는 0으로 설정

queue=deque()
queue.append(X)

while queue:
    #now==1
    now= queue.popleft()

    for next_n in graph[now]:
        if distance[next_n]==-1:
            distance[next_n]=distance[now]+1
            queue.append(next_n)

check=False #-1 출력을 위한 변수
for i in range(1,N+1):
    if distance[i]==K:
        print(i)
        check=True

if check==False:
    print(-1)
