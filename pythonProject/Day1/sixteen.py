n=6
for i in range(1,6):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(n,1,-1):
        print("*  ",end=" ")
    n-=1
    print()