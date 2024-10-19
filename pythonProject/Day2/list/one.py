name=input("Enter name")
num=int(input("Enter num"))
marks=float(input("Enter marks"))

li=[]
li.append(name)
li.append(num)
li.append(marks)
print(li)

name1=input("Enter name")

li.insert(1,name1)
print(li)

num1=int(input("Enter num"))
li.append(num1)

print(li)
