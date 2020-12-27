T=int(input())

if 1<=T<=1000:
    for i in range(T):
        c = 0
        N=int(input())
        if 1<=N<=1000000:
            while(N!=0):
                c=c+N%10
                N=int(N/10)

            print(c)

