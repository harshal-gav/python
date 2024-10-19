s = 'google.com'
frequency = {}

for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)