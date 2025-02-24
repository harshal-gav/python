class MyNumber:
    def __iter__(self):
        print("inside iter")
        self.num = 1
        return self

    def __next__(self):
        print("inside next")
        if self.num <= 10:
            temp = self.num
            self.num += 1
            return temp
        else:
            raise StopIteration


ref1 = MyNumber()
""" for i in ref1:          # here for loop invokes "__iter__()" first and then "__next__()" every time.
    print(i) """

# if you don't want to use for loop

try:
    ref1.__iter__()
    while 1:
        print(ref1.__next__())
except StopIteration as s:
    print("done with next")

print("done")

