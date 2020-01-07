# ! use python3
# string method exercise

VOWEL = ('a', 'e', 'i', 'o', 'u', 'y')
piglatin = []
print('Enter a str:\n')
one_str = input()

for word in one_str.split():
    prefix = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix += word[0]
        word = word[1:]

    if len(word) == 0:
        piglatin.append(prefix)
        continue

    suffix = ''
    while not word[-1].isalpha():
        suffix += word[-1]
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    prefixNonvowel = ''
    while len(word) > 0 and not word[0].lower() in VOWEL:
        prefixNonvowel += word[0]
        word = word[1:]

    if prefixNonvowel != '':
        word += prefixNonvowel + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()

    if wasTitle:
        word = word.title()

    piglatin.append(prefix + word + suffix)

    
print(' '.join(piglatin))

    

