#도시찾기(dfs)

from collections import deque
from sys import stdin

n,m,k,x = map(int,stdin.readline().split())

#그래프 정의
graph = list([] for _ in range(n+1))

#도시 간의 거리 표시
distance = [-1] * (n+1)
distance[x] = 0

#그래프에 연결 상태 입력
for _ in range(m):
    a,b = map(int,stdin.readline().split())
    graph[a].append(b)
    
#시작 지점에서부터 거리 계산
def solution(start,gap):
    q = deque([start])
    while q:
        now = q.popleft()   #현재 노드 위치 조회
        for next in graph[now]: #현재 노드와 연결된 노드 조회
            if distance[next] == -1:    #만약 연결되어 있다는 처리가 되지 않았다면
                distance[next] = distance[now] + 1  #연결 처리(거리 +1)
                q.append(next)

    #거리 k에 해당하는 도시 조회
    check = False
    for i in range(1, n+1):
        if distance[i] == gap:
            check = True 
            print(i)                
    if check == False:
        print(-1)
        
print(solution(x,k))