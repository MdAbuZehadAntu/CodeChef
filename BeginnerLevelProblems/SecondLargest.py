T=int(input())
ls=list()
for i in range(T):
    a,b,c=map(int,input().split())
    ls=[a,b,c]
    ls.sort()
    print(ls[1])



