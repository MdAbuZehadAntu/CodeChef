T = int(input())
for i in range(T):
    N = int(input())
    p = N % 10
    while N >= 10:
        N = int(N / 10)
    print(int(N) + p)
