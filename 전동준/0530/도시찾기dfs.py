#bfs 알고리즘
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
    
def solution(graph,start,visited):
    idx = 0 
    for i in graph[start]:
        if idx == visited:
            continue
        if not graph[i]:
            solution(graph,i,visited)
            idx += 1
    return visited[visited]
        
    
print(solution(graph,x,k))