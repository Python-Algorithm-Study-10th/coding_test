#dfs

from sys import stdin

n = map(int,stdin.readline().split())
numlist = list(map(int,stdin.readline().split()))
ca = list(map(int,stdin.readline().split()))

def solution(num,depth,total,cacount):
    plus = cacount[0]
    minus = cacount[1]
    multiply = cacount[2]
    divide = cacount[3]
    ans = []
    if depth == len(num):
        ans.append(max(total))
        ans.append(min(total))
        return
    if plus > 0:
        solution(num,depth+1, total+num[depth],[plus-1,minus,multiply,divide])
    if minus > 0:
        solution(num,depth+1, total-num[depth],[plus,minus-1,multiply,divide])
    if multiply > 0:
        solution(num,depth+1, total*num[depth],[plus,minus,multiply-1,divide])
    if divide > 0:
        solution(num,depth+1, int(total/num[depth]),[plus,minus,multiply,divide-1])
        
answer = solution(numlist,1,numlist[0],ca)
print(*answer,sep='\n')