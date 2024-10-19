class MyClass:
    def __init__(self,x):
        self.x = x
    def __gt__(self, other):
        return self.x > other.x
    def __lt__(self, other):
        return self.x < other.x
    def __eq__(self, other):
        return self.x == other.x
s1=MyClass(2)
s2=MyClass(3)
print( s1 > s2)
print(s1 < s2)
print(s1==s2)