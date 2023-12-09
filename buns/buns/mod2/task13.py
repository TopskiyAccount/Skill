barcode = input()
barcode = barcode.replace(" ", "")

if barcode.isdigit() and len(barcode) == 13:
    digits = [int(digit) for digit in barcode]
    odd_digits = digits[::2]
    even_digits = digits[1::2]
    odd_sum = sum(odd_digits)
    even_sum = sum(even_digits)
    if (odd_sum + 3 * even_sum) % 10 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
