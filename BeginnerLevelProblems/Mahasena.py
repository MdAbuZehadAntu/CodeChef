n=int(input())

ls=list(int(num) for num in map(int,input().strip().split()[:n]))
ev=0
od=0

for i in ls:
    if i%2==0:
        ev+=1
    else:
        od+=1

if ev>od:
    print("READY FOR BATTLE")
else:
    print("NOT READY")