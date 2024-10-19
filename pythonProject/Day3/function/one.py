def add():
    print("Add")
def modify():
    print("modify")
def delete():
    print("delete")

i=int(input("Enter number 1,2,3"))
match i:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("Wrong value")