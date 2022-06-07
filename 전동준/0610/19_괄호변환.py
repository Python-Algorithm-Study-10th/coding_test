from sys import stdin

def solution(p):
    answer = ''
    #1.빈 문자열인 경우 빈 문자열 반환
    if len(w) == 0:
        return answer
    #2.균형잡힌 문자열 u,v로 분리
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    #3.문자열 이어 붙이기
    if checker(u):  #u가 True(균형잡힌 문자열)이면
        answer = u + solution(v)
    else:   #u가 False(균형이 깨진 문자열)이면
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

w = stdin.readline()
solution(w)
    
#2-1.분리 기준
def balanced_index(p):  #'('와 ')'가 짝이 맞는지 확인
    count = 0   #왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
#3-1.올바른 문자열인지 확인
def checker(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:   #')'일 때
            if count == 0:  #count가 0인지 먼저 확인해줘야 함
                return False
            count -= 1        
    return True
        