#구글링 결과
from sys import stdin

def solution(s):
    result=[]
    if len(s)==1:
        return 1
     #이중 for 문(i는 문자열 앞부분, j는 앞부분을 제외한 나머지 부분)
    for i in range(1, (len(s)//2)+1):
        b = ''
        cnt = 1
        tmp=s[:i]
        for j in range(i, len(s), i):
            if tmp==s[j:i+j]:   #반복되는 문자열인 경우
                cnt+=1  #반복 횟수(숫자) +1
            else:   #반복되는 문자열이 아닌 경우
                if cnt!=1:  #이미 2회 이상 반복된 문자열이 있는 경우
                    b = b + str(cnt)+tmp    #최종 문자열 = 반복 횟수 + 반복된 문자열 + 나머지 문자열
                else:   #반복된 문자열이 없는 경우(규칙성이 전혀 없는 경우)
                    b = b + tmp #최종 문자열 == 원본 문자열
                tmp=s[j:j+i]
                cnt = 1
        if cnt!=1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
                
        result.append(len(b))
    return min(result)

#직접 작성해 본 코드
def solution(letter):
    for i in range(len(letter)//2+1):
        strs = letter[:i]
        rept = 1
        for j in range(i,len(letter),i):
            if strs == letter[j:i+j]:
                rept += 1
            
#리스트를 문자열로 바꾸기 : str = ''.join(list)