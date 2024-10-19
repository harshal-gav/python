a=1
print(a)
b=2
print(b)
for i in range(3,11):
    c=a+b
    a=b
    b=c
    print(c)
"""arr=[0,1]
for i in range(2,11):
    arr.append(arr[i-1]+arr[i-2])

print(arr)"""