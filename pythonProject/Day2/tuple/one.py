
list = [10, 20, 30, (40,50), 60]
count=0
for i in list:
    if isinstance(i,tuple):
        break
    else:
        count+=1
print(count)
