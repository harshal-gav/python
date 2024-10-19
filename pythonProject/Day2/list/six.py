li=[]
for i in range(1,6):
    num=int(input("Enter number"))
    li.append(num)
num=int(input("Enetr position to remove"))
li.pop(num)
print(li)