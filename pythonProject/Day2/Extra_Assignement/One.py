num1=int(input('Enter how many days in a month'))
num=int(input('Enter what day begin in month'))
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(" ".join(days_of_week))


print("    " * num, end="")

for day in range(1, num1 + 1):
    print(f"{day:>3}", end=" ")

    if (num + day) % 7 == 0:
            print()