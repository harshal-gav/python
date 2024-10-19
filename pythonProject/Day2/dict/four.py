people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
a=0
for i in people:
    a+=1
print(a)

people.update({'Lisa':'purple'})
print(people)

remove=people.pop('Jenny')
print(remove)

print(dict(sorted(people.items(),reverse=True)))
