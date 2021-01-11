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
    else:

        # print(ar)

        if b == d:

            if "D" in ar[b - 1, c - 1:e]:
                print("NO")
            else:
                print("YES")

        elif c == e:

            if "D" in ar[b - 1:d - 1, c - 1]:
                print("NO")
            else:
                print("YES")


        elif c < e:
            if "D" not in ar[b - 1, c - 1:e]:
                if "D" not in ar[b - 1:d - 1, e - 1]:
                    print("YES")
                elif "D" not in ar[b - 1:d - 1, c - 1]:
                    if "D" not in ar[d - 1, c - 1:e]:
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")

            elif "D" not in ar[b - 1:d - 1, c - 1]:
                if "D" not in ar[d - 1, c - 1:e]:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
