size = int(input())

matrix = [[i for i in range(1, size + 1)] for _ in range(size)]

for row in matrix:
    print(*row, sep=', ')

print()

for i in range(size):
    for j in range(i, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row, sep=', ')
