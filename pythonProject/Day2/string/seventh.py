def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    sentence_set = set(sentence.lower())

    return alphabet.issubset(sentence_set)



sentence = input("Enter a sentence: ")

if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")

