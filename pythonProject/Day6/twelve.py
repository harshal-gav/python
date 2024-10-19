import numpy as np

arr = np.array([[10, 20, 30, 40],
                 [50, 60, 70, 80],
                 [90, 100, 110, 120]])

print("a) 50, 60, 70, 80:")
print(arr[1, :])

print("\nb) 100 and 110:")
print(arr[2, 1:3])


print("\nc) 30, 70, and 110:")
print(arr[[0, 1, 2], [2, 2, 1]])


print("\nd) 50, 60, 90, and 100:")
print(arr[[1, 1, 2, 2], [0, 1, 0, 1]])  
