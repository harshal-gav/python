str=input("Enter string")
vowel=set('aeiouAEIOU')
count=0
for i in str:
    if i in vowel:
        count+=1
print(count)
