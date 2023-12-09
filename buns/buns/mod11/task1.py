import numpy as np

def matrix_multiply(a, b):
    # Проверяем, что количество столбцов в a равно количеству строк в b
    if len(a[0]) != len(b):
        raise ValueError("Невозможно умножить матрицы: неправильные размерности")

    result = [[0] * len(b[0]) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

# Генерация случайных матриц
a = np.random.sample((3, 3))
b = np.random.sample((3, 3))

# Умножение без использования NumPy
result_without_numpy = matrix_multiply(a.tolist(), b.tolist())
print("Результат без NumPy:")
print(result_without_numpy)

# Умножение с использованием NumPy
result_with_numpy = np.dot(a, b)
print("\nРезультат с NumPy:")
print(result_with_numpy)
