import math
t=int(input())
ls=list()
if t<=math.pow(10,6):
    for i in range(t):
        n=int(input())
        if(0<=n<=math.pow(10,6)):
            ls.append(n)
            

    ls.sort()
for i in ls:
    print(i)


