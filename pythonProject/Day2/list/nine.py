li=[]
for i in range(1,6):
    name=input("Enter name")
    li.append(name)

li.sort()
print(li)

li.sort(reverse=True)
print(li)