alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
lphbet = alphabet
for vowel in vowels:
    lphbet = lphbet.replace(vowel, "")

print(lphbet)

favourtieAlphabet = alphabet
favouriteLetters = 'gsbrox'

for letter in favouriteLetters:
    favourtieAlphabet = favourtieAlphabet.replace(letter, letter.upper())

print(favourtieAlphabet)