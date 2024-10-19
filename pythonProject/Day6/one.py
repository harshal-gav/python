import numpy as np
li=list()
for i in range(0,5):
    num=int(input("Enter number"))
    li.append(num)
print(li)

arr=np.array(li)
print(arr)
print(type(arr))
