from functools import reduce

li=[1,2,3,4,5]
mul=1
for i in li:
    mul*=i
print(mul)

print(reduce(lambda y,x:y*x,li))