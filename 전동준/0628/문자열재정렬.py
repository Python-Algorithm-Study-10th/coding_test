from sys import stdin

def solution(letter):
    letterboxa = []
    letterboxn = []
    #ord '1'은 49부터
    for i in range(len(letter)):
        if ord(letter[i]) >= 65:
            letterboxa.append(ord(letter[i]))
        else:
            letterboxn.append(int(letter[i]))
    letterboxa.sort()
    
    for i in range(len(letterboxa)):
        letterboxa[i] = chr(letterboxa[i])

    for i in letterboxa:
        print(i,end='')
    print(sum(letterboxn))

s = str(stdin.readline().strip())

solution(s)

#참고용
s=input()
c=[]
nsum=0
for i in s:
    if i.isdigit()==False:
        c.append(i)
    else:
        nsum+=int(i)
c.sort()
result="".join(c)
print(result+str(nsum))