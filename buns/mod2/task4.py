decimal_number = input()
hex_digits = "0123456789ABCDEF"
binary = ''
octal = ''
hexadecimal = ''
if decimal_number.isdigit() and int(decimal_number) > 0:
    decimal_number = int(decimal_number)
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary
        decimal_number //= 2
    n1 = int(decimal_number)
    while n1 > 0:
        octal = str(n1 % 8) + octal
        n1 //= 8
    n2 = int(decimal_number)
    while n2 > 0:
        hexadecimal = hex_digits[n2 % 16] + hexadecimal
        n2 //= 16
    print(binary, octal, hexadecimal)
else:
    print("Неверный ввод")
