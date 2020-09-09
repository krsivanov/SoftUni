text = input()

vowels = ['a', 'o', 'u', 'e', 'i']

no_vowels_text = [ch for ch in text if ch.lower() not in vowels]
print(''.join(no_vowels_text))
