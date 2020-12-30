import math
T=int(input())
ls=[int(math.pow(2,i-1)) for i  in range(12,0,-1)]
for i in range(T):
    p=int(input())
    c=0
    for it in ls:
        if it<=p:
            c+=int(p/it)
            p=p%it
    print(c)

