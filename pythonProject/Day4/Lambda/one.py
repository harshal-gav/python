def square(num):
    return num*num
print(square(2))

ref=(lambda x: x*x)(4)
print(ref)
print(square(2))