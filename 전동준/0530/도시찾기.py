#  DFS로 푸는 건 알겠는데...

from sys import stdin
from collections import deque

n,m,k,x = map(int,stdin.readline().split())
graph = [[] for _ in range(n + 1)]      # n이 아니라 n+1을 쓰는 이유?

for i in range(m):
    a,b = map(int,stdin.readline().split())
    graph[a].append(b)  # 도시 a가 b에 연결되어 있음을 graph 리스트에 기록
    
distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:  # 결과 없음(-1)을 표현하기 위한 구문
    print(-1)