import numpy as np

start = float(input("Enter the start value: "))
end = float(input("Enter the end value: "))
num_elements = int(input("Enter how many numbers to generate: "))

array = np.linspace(start, end, num_elements)

print("\nGenerated numpy array:")
print(array)
