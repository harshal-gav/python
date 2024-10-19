Students = {'d 01': 'Abc', 'd 0 2': 'Xyz', 'd0 3': 'Pqr'}

cleaned_students = {key.replace(" ", ""): value for key, value in Students.items()}

print(cleaned_students)