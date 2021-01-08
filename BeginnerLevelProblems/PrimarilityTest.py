T=int(input())

for i in range(T):
    N=int(input())
    flag=0
    for i in range(2,int(N/2)+1):
        if N%i==0:
            flag=1

    if flag==0:
        print("yes")
    else:
        print("no")