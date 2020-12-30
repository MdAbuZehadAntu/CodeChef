N=int(input())
L=0
p=0
q=0
for i in range(N):
    S,T=map(int,input().split())
    p+=S
    q+=T
    d=p-q
    if d>0 and (L<p-q):
            L=p-q
            W=1;
    elif d<0 and L<q-p:
            L= abs(q - p)
            W = 2;

print(W,L)