from collections import deque
import sys
<<<<<<< Updated upstream

n,m,k,start=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)] # [ [](무시) [2,3] [3,4] [] []  ] 총 n+1개지만 처음 []은 무시하므로 n개
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
distance=[False for _ in range(n+1)] #만약 4일떄 [false(무시) false false false false] 0번노드부터 시작을 안하니 
                                    # 만약 n으로 하게되면 마지막노드를 표시할수없음.
                                    #distance는 0을 기준점으로 얼마나 떨어져있는지에대한 지표
# bfs풀이                            
def bfs():
    q=deque()
    q.append(start)           # 큐에는 기준이되는 좌표나 시작점을 넣는거!!
    distance[start]=0           # false 0 false false false  1번노드가 기준일떄 
    while q:
        now=q.popleft()         
        for next in graph[now]:   # 그래프에선 현위치를 기준으로 연결된 노드들을 나타내므로.
            if distance[next]==False: # False 라는것은 다른노드들은 아직 한번도 방문하지 않았으므로 
                distance[next]=distance[now]+1 # 방문하게되면 (방문한노드=현위치+1)이됨.
                q.append(next) # next를 큐에 추가하면 방문한곳을 기준으로 다시 그래프연결된 노드를 for문이 탐색

bfs() 

check=False
for i in range(len(graph)):
    if distance[i]==k: # 찾으려는값이 있으면
        print(i)  # 찾으려는값 노드출력
        check=True
if check==False: #찾으려는값 없으므로
    print(-1)


# dfs 풀이 
sys.setrecursionlimit(10**7) # 런타임에러나올떄 재귀의 최대깊이 제한 변경

distance[start]=0
def dfs(graph,start,distance):
    
    
    for next in graph[start]: # 2 3 
        if distance[next]==False:
            distance[next]=distance[start]+1
            
    for next in graph[start]: 
        dfs(graph,next,distance)

dfs(graph,start,distance)

check=False
for i in range(len(graph)):
    if distance[i]==k: # 찾으려는값이 있으면
        print(i)  # 찾으려는값 노드출력
        check=True
if check==False: #찾으려는값 없으므로
    print(-1)
=======
#도시개수,도로의개수,거리정보,출발도시번호
n,m,k,x=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
# 모든 도로 정보 입력받기
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)

# [ [] [2,3] [3,4], []  ]   # 값 
#   0    1     2     3         # index

#[ [1,2] [1,3] [2,3],[2,4 ] ]
# 0 1 2 3 index

#모든 도시에 최단 거리 초기화
distance=[False]*(n+1) #-1은 자신의 노드 방문시 0으로 만들기위함.
distance[x]=0 #x: start 
# [-1 0 -1 -1 -1]
def bfs(graph,x,distance):
    q=deque([x])
    while q:
        now=q.popleft() # index번호를 now로 둔거죠. 1
        #현재 도시 이동할수 있는 모든 도시 확인
        for next_node in graph[now]: # 2,3 
            #아직 방문안한 도시
            if distance[next_node]==False: 
                #최단 거리 갱신
                distance[next_node]=distance[now]+1 # 현재 위치
                q.append(next_node)
    
    #최단 거리 k인 모든 도시 번호를 오름차순 출력
    check=False
    for i in range(1,n+1): # distance에서 k인 노드찾기(오름차순이라서 1~n)
        if distance[i]==k:
            print(i)
            check=True
    #최단 거리 k인 도시 없으면 -1
    if check==False:
        print(-1)        

bfs(graph,x,distance)
>>>>>>> Stashed changes
