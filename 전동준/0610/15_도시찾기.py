#도시찾기(bfs)

from collections import deque
from sys import stdin

n,m,k,x = map(int,stdin.readline().split())

#그래프 정의
graph = list([] for _ in range(n+1))

#출발 도시(x)와의 거리 표시
distance = [-1] * (n+1)
distance[x] = 0

#그래프에 연결 상태 입력
for _ in range(m):
    a,b = map(int,stdin.readline().split())
    graph[a].append(b)
    
#시작 지점에서부터 거리 계산
def solution(graph1,graph2,start,goal):     #연결도 그래프, 거리 표시 그래프, 시작 지점, 목표 거리
    q = deque([start])
    while q:
        now = q.popleft()   #현재 노드 위치 조회
        for next in graph1[now]: #현재 노드와 연결된 노드 조회
            if graph2[next] == -1:    #만약 연결되어 있다는 처리가 되지 않았다면
                graph2[next] = graph2[now] + 1  #연결 처리(거리 +1)
                q.append(next)

    #거리 goal에 해당하는 도시 조회
    check = False
    asw = []
    for i in range(1, n+1):
        if graph2[i] == goal:
            check = True 
            asw.append(i)
    if check == False:
        return -1
    else:
        return asw

answer = solution(graph,distance,x,k)
print(*answer,sep='\n')     #리스트로 저장된 값을 한 줄에 하나씩 반환