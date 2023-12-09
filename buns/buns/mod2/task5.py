input_data = input().split(',')
symbol = input_data[0]
shift = int(input_data[1])
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.index(symbol)
new_index = (index + shift) % 26
result = alphabet[new_index]
print(result)
