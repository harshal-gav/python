se=set({})
for i in range(1,11):
    num=int(input("Enter num"))
    se.add(num)
print(se)

num2=int(input("Enter num"))
se.discard(num2)

print(se)