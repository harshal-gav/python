class A:
    def __init__(self):
        print("A Constructor")
class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")
class C(A):
    def __init__(self):
        super().__init__()
        print("C constructor")
class D(A):
    def __init__(self):
        super().__init__()
        print("D constructor")
a=A()
b=B()
c=C()
d=D()

