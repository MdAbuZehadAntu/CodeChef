T=int(input())

for i in range(T):
    N=int(input())
    n=N
    rev=0
    while(N!=0):
        rev =(rev*10)+N%10
        N=int(N/10)
    if rev==n:
        print("wins")
    else:
        print("loses")