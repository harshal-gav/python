numbers_tuple = (5, 2, 9, 1, 6, 6)
hash=dict()
for i in numbers_tuple:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in hash:
    if hash[i]>1:
        print(i)
