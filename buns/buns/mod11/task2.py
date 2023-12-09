import numpy as np
import time

# Генерация случайных векторов
a = np.random.sample((3,))
b = np.random.sample((3,))

def scalar_product(a, b):
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s

def np_scalar_product(a, b):
    return np.dot(a, b)

# Засекаем время для обычного скалярного произведения
start_time = time.time()
product_1 = scalar_product(a, b)
end_time = time.time()
print("Время выполнения (обычное скалярное произведение):", end_time - start_time)

# Засекаем время для скалярного произведения с использованием NumPy
start_time = time.time()
product_2 = np_scalar_product(a, b)
end_time = time.time()
print("Время выполнения (NumPy скалярное произведение):", end_time - start_time)

# Проверка корректности
error = np.abs(product_1 - product_2).sum()
print("Погрешность:", error)

# Почему методы NumPy оказываются более эффективными: Векторизация операций. Оптимизированные алгоритмы. Управление памятью.
