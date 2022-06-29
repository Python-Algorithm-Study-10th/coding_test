# from sys import stdin

# def solution(score):
#     Score = str(score)
#     standard = len(Score) // 2
#     lefts = []
#     rights = []
#     for i in range(standard):
#         lefts.append(int(Score[i]))
#     for j in range(standard,len(Score)):
#         rights.append(int(Score[j]))
#     # lefts와 rights의 합이 동일하면 LUCKY 반환
#     if sum(lefts) == sum(rights):
#         return 'LUCKY'
#     else:
#         return 'READY'

# n = int(stdin.readline().strip())
# print(solution(n))

#참고용
import sys

n=list(map(int,sys.stdin.readline().strip()))

if len(n) %2 ==0:
    font_sum=0
    back_sum=0
    for i in range((len(n)//2)):
        font_sum+=n[i]
        back_sum+=n[len(n)-1-i]
    if font_sum == back_sum:
        print("LUCKY")
    else:
        print("READY")
else:
    print("READY")