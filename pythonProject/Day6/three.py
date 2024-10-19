import numpy as np

arr = np.array([
    ['H', 'G', '-'],
    ['-', 'H', 'G'],
    ['G', '-', 'H']
])


print("Initials in tabular form:")
for row in arr:
    print('\t'.join(row))
