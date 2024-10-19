from pandas import Series

marks = []
subjects = []

for i in range(5):
    subject = input(f"Enter the name of subject {i+1}: ")
    mark = float(input(f"Enter the marks for {subject}: "))
    subjects.append(subject)
    marks.append(mark)


subject_marks = Series(marks, index=subjects)

   
print(subject_marks)
