#미완성
from sys import stdin

def solution(letter):
    letcount = 0
    for i in range(len(letter)):
        for j in range(len(letter)):
            if letter[i:j+1] == letter[j+1:(j+1)+(j-i)+1] and letcount < len(letter[i:j+1]):
                letcount = len(letter[i:j+1])
    return letcount
    
    
    
s = list(str(stdin.readline().strip()))

print(solution(s))