key=[[0,0,0],[1,0,0],[0,1,1]]
lock=[[1,1,1],[1,1,0],[1,0,1]]

def rotate_90(ls):
    n=len(ls) # 행
    m=len(ls[0]) #열
    
    rotate_ls=[[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            rotate_ls[j][n-i-1] = ls[i][j]
    return rotate_ls

def rotate901(arr):
    return list(zip(*arr[::-1]))

print(rotate901(key))
def check(new_lock,n,m):
    for i in range(n):
        for j in range(n):
            if new_lock[i+m][j+m] != 1:
                return False
    return True

def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]
            
def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]
              
def solution(key,lock):
    m,n = len(key), len(lock)

     
    new_lock=[[0] * (m*2+n) for _ in range(m*2+n)]
    for i in range(n):
        for j in range(n):
            new_lock[i+m][j+m] = lock[i][j]
    for _ in range(4):
        key90=rotate_90(key)
        
        for x in range(1,m+n):
            for y in range(1,m+n):
                attach(x,y,m,key90,new_lock)
                
                if check(new_lock,n,m):
                    return True
                detach(x,y,m,key90,new_lock)
                

solution(key,lock)