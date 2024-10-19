class course:
    def start(self):
        print("Course Start")
    def end(self):
        print("Course End")
class MsCit(course):
    def start(self):
        print("MsCit Course Start")
    def end(self):
        print("MsCit Course End")
class Basic(course):
    def start(self):
        print("Basic Course Start")
    def end(self):
        print("Basic Course End")
class Dbda(course):
    def start(self):
        print("Dbda Course Start")
    def end(self):
        print("Dbda Course End")
    def orientation(self):
        print("DBDA orientation")

def perform(ref):
    ref.start()
    if isinstance(ref,Dbda):
        ref.orientation()
    ref.end()

perform(MsCit())
perform(Basic())
perform(Dbda())
