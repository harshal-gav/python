
for i in range(6):
    for j in range(6-i):
        print(" ",end='')
    u = 1
    for k in range(i):
        print(u,end='')
        u+=1
    for l in range(i-1,0,-1):
        print(l,end='')
    print()