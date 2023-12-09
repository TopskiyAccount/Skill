phone_number = input()
result = ''.join(char for char in phone_number if char.isdigit() or char == '+')
print(result)
