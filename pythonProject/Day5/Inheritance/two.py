class vehicle:
    def start(self):
        print("Vehicle starts")
class fourwheeler(vehicle):
    def start(self):
        print("fourwheeler starts")
f=fourwheeler()
f.start()