#dfs
#미완성

from sys import stdin

n = map(int,stdin.readline().split())
numlist = list(map(int,stdin.readline().split()))
ca = list(map(int,stdin.readline().split()))

maximum = -1e9
minimum = 1e9

def solution(num,depth,total,cacount):
    plus = cacount[0]
    minus = cacount[1]
    multiply = cacount[2]
    divide = cacount[3]
    global maximum,minimum
    if depth == len(num):
        maximum = max(total,maximum)
        minimum = min(total,minimum)
        return
    if plus > 0:
         solution(num,depth+1, total+num[depth],[plus-1,minus,multiply,divide])
    if minus > 0:
        solution(num,depth+1, total-num[depth],[plus,minus-1,multiply,divide])
    if multiply > 0:
        solution(num,depth+1, total*num[depth],[plus,minus,multiply-1,divide])
    if divide > 0:
        solution(num,depth+1, int(total/num[depth]),[plus,minus,multiply,divide-1])

solution(numlist,1,numlist[0],ca)
print(maximum)
print(minimum)