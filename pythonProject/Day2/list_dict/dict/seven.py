d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
for i,j in d1.items():
    d3[i]=j

for i,j in d2.items():
    if i in d3.keys():
        d3[i]+=j
    else:
        d3[i]=j
print(d3)