from collections import deque
from sys import stdin

n,m,k,x = map(int,stdin.readline().split())

graph = list([] * (n+1))
for i in range(m):
    a,b = map(int,stdin.readline().split())
    graph[a].append(b)

def solution():