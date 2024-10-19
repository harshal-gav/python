li1=[1,2,3,4,5,6,7]
li2=[5,6,7,8,9,0]
l=len(li1)-1
for i in li2:
    li1.insert(l,i)
    l+=1
li1.pop()
print(li1)
