input_string = input()
count_ones = 0
count_zeros = 0

for char in input_string:
    if char == '1':
        count_ones += 1
    elif char == '0':
        count_zeros += 1

if count_ones == count_zeros:
    print('yes')
else:
    print('no')
