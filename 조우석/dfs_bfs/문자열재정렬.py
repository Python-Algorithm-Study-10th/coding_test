import sys
text=list(map(str,sys.stdin.readline().strip()))
text.sort()
# print(text)
ls=[]
for j in range(ord('A'), ord('Z')+1):
    ls.append(chr(j))

sum=0
new_text=text.copy()

for i in new_text:
    if i not in ls:
        sum+=int(i)
        text.remove(i)
print(text)
str2="".join(text) #리스트 문자열 합치기 
print(str2+str(sum))