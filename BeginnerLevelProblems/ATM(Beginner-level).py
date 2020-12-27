x,y=input().split()
x=int(x)
y=float(y)
if 0<x<=2000 and 0<=y<=2000:
    if x%5==0 and x<=y-0.5:
        print("{:.2f}".format(y-x-0.5))
    else:
        print("{:.2f}".format(y))


# arr = list(map(int, input().split()))
# print(arr)
# print(type(arr))