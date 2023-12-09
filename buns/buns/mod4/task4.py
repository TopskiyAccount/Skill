def palindrome(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    odd_count = 0
    odd_letter = ""
    for letter, count in letter_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_letter = letter

    if odd_count > 1:
        return None


    palindrome = ""
    for letter, count in letter_count.items():
        half_count = count // 2
        palindrome += letter * half_count

    if odd_count == 1:
        palindrome += odd_letter

    return palindrome + palindrome[::-1]

# Ввод слова
word = input("Введите слово: ")

result = palindrome(word)
if result:
    print("Можно составить палиндром:", result)
else:
    print("Невозможно составить палиндром из данного слова.")
