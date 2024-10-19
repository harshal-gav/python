List = ['abc', 'xyz', 'aba', '1221']

for i in List:
   if(len(i)>1 and (i[:1]==i[-1:-2:-1])):
        print(i)


