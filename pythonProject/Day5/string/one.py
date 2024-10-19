
s = 'restart'

first_char = s[0]

result = first_char + s[1:].replace(first_char, '$')

print(result)
