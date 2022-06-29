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