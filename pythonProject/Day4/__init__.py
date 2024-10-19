""" sys.getrefcount(object)

Returns the reference count of the object. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to getrefcount(). """

import sys
class First:
    def __init__(self,num):
        self.num=num

f1=First(100)
f2=f1
f3=f2
print(f1.num)
print(sys.getrefcount(f1))    #  4
del f2
print(sys.getrefcount(f3))    #  3

""" When you call getrefcount(), the reference is copied by value into the function's argument, temporarily bumping up the object's reference count. This is where the second reference comes from. """