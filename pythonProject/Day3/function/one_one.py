def show1():
    print("Function show1 invoked.")

def show2():
    print("Function show2 invoked.")

def show3():
    print("Function show3 invoked.")

def caller(func):
    func()

caller(show1)
caller(show2)
caller(show3)
