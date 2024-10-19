from operator import index

List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
List2=[]
for i in range(len(List)):
    if i!=0 and i!=4 and i!=5:
        List2.append(List[i])
print(List2)