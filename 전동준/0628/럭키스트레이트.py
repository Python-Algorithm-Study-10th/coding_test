from sys import stdin

def solution(score):
    Score = str(score)
    standard = len(Score) // 2
    lefts = []
    rights = []
    for i in range(standard):
        lefts.append(int(Score[i]))
    for j in range(standard,len(Score)):
        rights.append(int(Score[j]))
    # lefts와 rights의 합이 동일하면 LUCKY 반환
    if sum(lefts) == sum(rights):
        return 'LUCKY'
    else:
        return 'READY'

n = int(stdin.readline().strip())
print(solution(n))