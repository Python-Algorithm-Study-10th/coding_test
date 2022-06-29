import sys


text=list(map(str,sys.stdin.readline().strip()))
answer=len(text)

if answer == 1:
    print(1)

for step in range(1, len(text) // 2 + 1):
    temp = ""
    prev = text[0:step]
    count = 1
    for i in range(step, len(text), step):
        if prev == text[i:i + step]: #text[6:7]
            count += 1
        else:
            prev="".join(prev)
            if count >= 2:
                temp += str(count) + prev
            else:
                temp+=prev
            prev = text[i:i + step]
            count = 1
            
    prev="".join(prev)
    if count >= 2:
        temp += str(count) + prev 
    else:
        temp+=prev
    answer = min(answer, len(temp))
print(answer)