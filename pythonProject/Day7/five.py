import pandas as pd

names = []
designations = []
salaries = []

for i in range(5):
    name = input(f"Enter name of employee {i + 1}: ")
    designation = input(f"Enter designation of employee {i + 1}: ")
    salary = float(input(f"Enter salary of employee {i + 1}: "))

    names.append(name)
    designations.append(designation)
    salaries.append(salary)

data = {
    'Name': names,
    'Designation': designations,
    'Salary': salaries
}
df = pd.DataFrame(data)

print("\nEmployee Data:")
print(df)
