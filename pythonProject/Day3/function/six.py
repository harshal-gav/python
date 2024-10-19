def toggle_case(char):
    if char.islower():
        return char.upper()
    elif char.isupper():
        return char.lower()
    else:
        return char  # If the input is not a letter, return it unchanged

char = 'a'
print(toggle_case(char))

char = 'Z'
print(toggle_case(char))

char = '1'
print(toggle_case(char)) 
