import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])

# a) Find common elements in both arrays
common_elements = np.intersect1d(arr1, arr2)
print(common_elements)

# b) Find unique elements of the first array (elements in arr1 but not in arr2)
unique_in_arr1 = np.setdiff1d(arr1, arr2)
print(unique_in_arr1)

# c) Find unique elements of the second array (elements in arr2 but not in arr1)
unique_in_arr2 = np.setdiff1d(arr2, arr1)
print(unique_in_arr2)
