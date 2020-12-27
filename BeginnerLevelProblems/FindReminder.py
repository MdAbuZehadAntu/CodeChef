T=int(input())

if 1<=T<=1000:
    for i in range(T):

        A,B=map(int,input().split())
        if 1<=A<=10000 and 1<=B<=10000:
            print(A%B)

