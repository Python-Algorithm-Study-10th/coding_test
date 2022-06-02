#dfs 알고리즘
#문제 특성 상 dfs는 비효율적
from collections import deque
from sys import stdin

n,m,k,x = map(int,stdin.readline().split())
graph = []
graph = [[] for i in range(n+1)]



for i in range(m):
    a,b = map(int,stdin.readline().split())
    graph[a].append(b)

visited = [False] * (n+1)
visited[x] = True
distance = [[-1] for _ in range (n+1)]
distance[x] = 0
    
def solution(graph,start,k):
    idx = 0
    for i in graph[start]:
        if idx == visited:
            continue
        if not visited[i]:
            solution(graph,i,k)
            idx += 1
    return visited[k]
        
print(solution(graph,x,k))