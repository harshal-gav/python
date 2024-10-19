n=5
for i in range(1,6):
    for j in range(1,n):
        print(" ",end="")
    n-=1
    for k in range(1,i):
        print(" *",end="")
    print()