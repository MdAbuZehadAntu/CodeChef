T=int(input())

for i in range(T):
    A,B=map(int,input().split())
    print(max(A,B),A+B)