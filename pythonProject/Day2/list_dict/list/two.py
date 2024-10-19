words = ["apple", "banana", "grape", "watermelon", "kiwi", "orange"]

n = int(input("Enter the length n: "))

words2=[w for w in words if len(w)>n]

print(words2)