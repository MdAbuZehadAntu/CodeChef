import numpy as np

N, M, Q = map(int, input().split())
arr = []

for i in range(N):
    ls = []
    for j in range(M):
        ls.append("B")
    arr.append(ls)

arr = np.array(arr)
ar = arr.copy()
for i in range(Q):

    a, b, c, d, e = map(int, input().split())
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0

    if a == 1:

        if e == M:
            e = e - 1
        ar[b - 1, 1:e - 1] = "D"
        ar[b - 1:d, 1] = "D"
        ar[b - 1:d, e - 1] = "D"
        ar[d - 1, 1:e - 1] = "D"


print(ar)
print(ar[3,1:5:-1])