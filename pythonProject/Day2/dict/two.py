dict={"soap":100, "deo":300, "perfume":400}
a=input("Enter name of product")
a.lower()
if(dict.get(a)):
    print("Price of product is", dict.get(a))
else:
    print("There is not such product into dict")
