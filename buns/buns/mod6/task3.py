def get_armstrong_numbers():
    for num in range(10, 10**6):  
        num_str = str(num)
        power = len(num_str)
        if num == sum(int(digit)**power for digit in num_str):
            yield num

armstrong_generator = get_armstrong_numbers()
for i in range(8):
    print(next(armstrong_generator), end=' ')
