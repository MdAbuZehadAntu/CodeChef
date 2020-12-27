T=int(input())

for i in range(T):
    n=int(input())
    c=0
    while(n!=0):
        if n%10==4:
            c+=1
        n=int(n/10)
    print(c)

