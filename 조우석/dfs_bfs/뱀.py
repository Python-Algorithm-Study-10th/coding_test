import sys
from collections import deque

n=int(sys.stdin.readline()) 
graph=[[0] * n for i in range(n)]
apple=int(sys.stdin.readline().strip())

for _ in range(apple):
    x,y=map(int,sys.stdin.readline().split())
    graph[x-1][y-1]=2

L=int(sys.stdin.readline())
direct=deque()

for _ in range(L):
    time,direction=sys.stdin.readline().split()
    time=int(time)
    direct.append([time,direction])

dx=[1,-1,0,0]
dy=[0,0,-1,1]
turn_direct=1 # 1(동) 2(남) 3(서) 0(북))
def turn(direction):
    global turn_direct
    if direction=="L":
        turn_direct-=1
        if turn_direct<0:
            turn_direct=3
    elif direction=="D":
        turn_direct+=1
        if turn_direct>=4:
            turn_driect=0
    return turn_direct

snake=deque()
x,y=0,0
snake.append([x,y])
time=0
while True:
    time+=1
    x,y=snake.popleft()
    if turn_direct==1: # 동쪽이면
        nx=x+dx[3]
        ny=y+dy[3]
    elif turn_direct==2:
        nx=x+dx[1]
        ny=y+dy[1]
    elif turn_direct==3:
        nx=x+dx[2]
        ny=y+dy[2]
    elif turn_direct==3:
        nx=x+dx[0]
        ny=y+dy[0]
    if time == direct[0][0]:
        a,b=direct.popleft()
        turn(b)
        snake.append((nx,ny))
        time-=1
        continue
        
    if nx>=n or ny>=n or nx<0 or ny<0:
        break
        
    if graph[nx][ny] == 0: #사과아니고 지난적없음.
        snake.append((nx,ny))
        graph[nx][ny]=1 #  지나감
    elif graph[nx][ny] ==2: # 사과이면
        snake.append((nx,ny))
        graph[nx][ny] = 1 
print(time)