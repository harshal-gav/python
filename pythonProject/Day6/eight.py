import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

print("Array 1:")
print(arr1)
print("Array 2:")
print(arr2)

sum_axis_0 = np.sum([arr1, arr2], axis=0)

print(sum_axis_0)

sum_axis_1 = np.sum([arr1, arr2], axis=1)
print("\nSum along axis=1 (row-wise sum):")
print(sum_axis_1)

stacked = np.stack((arr1, arr2), axis=2)
sum_axis_2 = np.sum(stacked, axis=2)
print("\nSum along axis=2 (depth-wise sum after stacking):")
print(sum_axis_2)
