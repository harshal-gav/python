

str=input("Enter string")
str.lower()
if(str==str[::-1]):
    print("String is palindrome")
else:
    print("String is not palindrome")
