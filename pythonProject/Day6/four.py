import numpy as np

numbers_list = []

for i in range(12):
    num = int(input(f"Enter number {i+1}: "))
    numbers_list.append(num)

one_d_array = np.array(numbers_list)

print("One-dimensional array:")
print(one_d_array)

two_d_array = one_d_array.reshape(4, 3)

print("\nTwo-dimensional (4x3) array:")
for row in two_d_array:
    print('\t'.join(map(str, row)))
