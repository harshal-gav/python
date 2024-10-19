import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

print("Original 2D array:")
print(arr)

num = float(input("\nEnter a number: "))

addition = arr + num
subtraction = arr - num
multiplication = arr * num
division = arr / num
modulus = arr % num
exponentiation = arr ** num
floor_division = arr // num

print("\nArray after addition:")
print(addition)

print("\nArray after subtraction:")
print(subtraction)

print("\nArray after multiplication:")
print(multiplication)

print("\nArray after division:")
print(division)

print("\nArray after modulus:")
print(modulus)

print("\nArray after exponentiation:")
print(exponentiation)

print("\nArray after floor division:")
print(floor_division)
