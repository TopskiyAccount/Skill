input_str = input()
vowels = "аеёиоуыэюяaeiou"
consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"

vowel_count = 0
consonant_count = 0

for char in input_str:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print(vowel_count, consonant_count)
