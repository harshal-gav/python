class Base:
    def __init__(self,num):
        print(num)
class Sub(Base):
    def __init__(self,num):
        super().__init__(num)
Sub(10)