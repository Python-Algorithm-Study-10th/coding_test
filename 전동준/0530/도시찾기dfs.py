#bfs 알고리즘
from collections import deque
from sys import stdin

n,m,k,x = map(int,stdin.readline().split())
graph = []
graph = [[] for i in range(n+1)]



for i in range(n+1):
    a,b = map(int,stdin.readline().split())
    graph[a].append(b)
    
count = 0

def solution(graph,start,distance):
    q = deque(start)
    visited = [False] * (n+1)
    visited[x] = True
    while q:
        for i in distance[start]:
            if not distance[i]:
                solution(graph,i,distance,distance)
        distance -= 1
        if distance == 0:
            return q
    
print(solution(graph,x,k))