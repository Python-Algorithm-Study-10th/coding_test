import sys 
from itertools import combinations
          
n,m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
ls=[] # 치킨집 좌표 모음
home=[] # 집 좌표 모음

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2: 
            ls.append((i,j))
        if graph[i][j] == 1:
            home.append((i,j))
chicken= list(combinations(ls,m)) # 치킨집 m개 뽑을떄 모든조합 나옴


min_distance=sys.maxsize #엄청큰수 설정
for item in chicken:
    home_distance=0
    for i in range(len(home)): # 집좌표 와 치킨집좌표 길이 구하려고 
        tmp=sys.maxsize # 엄청큰수 설정
        for x,y in item:
            tmp = min(tmp,abs(x-home[i][0])+ abs(y-home[i][1])) # 치킨집과 집 까지 거리중 최소
        home_distance+=tmp # 최소값을 더함 
    min_distance=min(min_distance,home_distance)
print(min_distance)

            
      
            
            