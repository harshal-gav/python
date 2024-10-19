a=input("Enter character")
a.lower()
match a:
    case 'a':
        print('A is vowel')
    case 'e':
        print('E is vowel')
    case 'i':
        print('I is vowel')
    case 'o':
        print('O is vowel')
    case 'u':
        print('U is vowel')
    case _:
        print('Not Vowel')
