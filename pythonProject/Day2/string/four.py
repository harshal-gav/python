input=input("Enter string")

char_dict={}

for i in input:
    if i in char_dict:
        char_dict[i] += 1
    else:
        char_dict[i] = 1

for i in char_dict:
    if char_dict[i]>1:
        print(i)


