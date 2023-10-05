input_str = input()
numbers = input_str.split()
numbers = [int(num) for num in numbers]
unique_numbers = []
has_duplicates = False
for num in numbers:
    if num in unique_numbers:
        has_duplicates = True
        break
    else:
        unique_numbers.append(num)

print(has_duplicates)
