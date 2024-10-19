class Student:
    def __init__(self,name,age,addr,quli):
        self.name=name
        self.age=age
        self.addr=addr
        self.quli=quli

    def __str__(self):
        return "name is="+self.name+" age is="+str(self.age)+" addr is="+self.addr+" quli is="+self.quli


a=Student("Harshal",22,"Sangli","Btech")
b=Student("Ravi",34,"Virar","abc")
c=Student("Max",26,"Dutch","Driver")
d=Student("Leclerc",45,"Monaco", "Driver")

dict={1:a,2:b,3:c,4:d}

num=int(input("Enter roll no "))
if(dict.get(num)):
    print(dict.get(num))
else:
    print("Student not found")

