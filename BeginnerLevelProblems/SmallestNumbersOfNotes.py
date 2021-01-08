ls=[100,50,10,5,2,1]

T=int(input())

for i in range(T):
    N=int(input())
    p = 0
    for item in ls:
        if(N!=0):
            p+=int(N/item)
            N=N%item

    print(p)

