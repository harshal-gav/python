# Bar plot
from matplotlib import pyplot as py

students={"Sachin":90,"Rahul":80,"Anil":70}

names=list(students.keys())
marks=list(students.values())

# py.bar(names,marks)
py.barh(names,marks)
py.xlabel("Students names")
py.ylabel("marks in maths")
py.show()

