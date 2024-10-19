import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

arr = np.zeros((rows, cols))

print(f"\nEnter the elements for a {rows}x{cols} array:")
for i in range(rows):
    for j in range(cols):
        arr[i][j] = float(input(f"Element [{i+1}, {j+1}]: "))

print("\nTwo-dimensional array:")
print(arr)

sum_axis_0 = np.sum(arr, axis=0)

sum_axis_1 = np.sum(arr, axis=1)

print("\nSum along axis=0 (column-wise sum):", sum_axis_0)
print("Sum along axis=1 (row-wise sum):", sum_axis_1)
