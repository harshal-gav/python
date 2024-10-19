key=int(input("Enter key"))
dict={1:34,2:45,3:87}

for i in dict.keys():
    if i==key:
        print("This is a key")
        break
    else:
        print("This is not key")
        break