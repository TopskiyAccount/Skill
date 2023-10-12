with open("input1.txt", "r") as file:
    field = [line.strip() for line in file]

def check_win(player, field):
    size = len(field)
    for i in range(size):
        if all(field[i][j] == player for j in range(size)):
            return True
        if all(field[j][i] == player for j in range(size)):
            return True
    if all(field[i][i] == player for i in range(size)):
        return True
    if all(field[i][size - i - 1] == player for i in range(size)):
        return True
    return False

if check_win("X", field):
    result = "X"
elif check_win("O", field):
    result = "O"
else:
    result = "Ничья"

with open("output1.txt", "w") as output_file:
    output_file.write(result)
