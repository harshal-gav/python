import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])


stack_axis_0 = np.vstack((arr1, arr2))
print("Stacked along axis=0 (vstack):")
print(stack_axis_0)

stack_axis_1 = np.hstack((arr1, arr2))
print("Stacked along axis=1 (hstack):")
print(stack_axis_1)

# Stack along axis=2 (depth stacking, adding a new dimension)
stack_axis_2 = np.stack((arr1, arr2), axis=2)
print("Stacked along axis=2 (stack):")
print(stack_axis_2)
