def frequency(filename):
    letter_frequency = {}
    
    with open(filename, 'r') as file:
        for line in file:
            for letter in line:
                if letter.isalpha(): 
                    if letter in letter_frequency:
                        letter_frequency[letter] += 1
                    else:
                        letter_frequency[letter] = 1
    
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1])
    
    return sorted_frequency

filename = input("Введите имя файла: ")

try:
    result = frequency(filename)

    with open("result.txt", 'w') as output_file:
        for letter, frequency in result:
            output_file.write(f"{letter}: {frequency}\n")
    
    print("Результат успешно сохранен в файл result.txt")
except FileNotFoundError:
    print("Файл не найден.")
