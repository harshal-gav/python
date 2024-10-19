n=6
m=5
for i in range(1,7):
    for j in range(1,n):
        print(" ",end=" ")
    n-=1
    for k in range(1,i):
        print("*  ",end=" ")
    print()

for p in range(1,5):
    for o in range(1,p+1):
        print(" ",end=" ")
    for l in range(1,m):
        print("*  ", end=" ")
    m-=1
    print()
