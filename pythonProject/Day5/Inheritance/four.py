class Top1:
    def disp(self):
        print("Display")
class Bottom1(Top1):
    def disp(self):
        print("Bottom 1 Display")
class Bottom2(Top1):
    def disp(self):
        print("Bottom 2 Display")
class Bottom3(Top1):
    def disp(self):
        print("Bottom 3 Display")
def perform(ref):
    ref.disp()
perform(Bottom1())
perform(Bottom2())
perform(Bottom3())
