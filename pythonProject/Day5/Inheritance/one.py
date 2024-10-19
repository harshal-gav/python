class A:
    def __init__(self):
        super().__init__()
        print("Parent Class Constructor")
class B(A):
    def __init__(self):
        super().__init__()
        print("Child of Parent")
class C(B):
    def __init__(self):
        super().__init__()
        print("Child of Child")

c=C()