import numpy as np

# Функция, решающая задачу с помощью NumPy
def np_encode(a):
    # Используем функцию groupby из библиотеки itertools
    # для группировки последовательных элементов
    grouped_elements = [list(group) for key, group in groupby(a)]

    # Создаем массив из уникальных элементов
    unique_elements = np.array([key for key, _ in groupby(a)])

    # Создаем массив с количеством повторений для каждого элемента
    repetitions = np.array([len(group) for group in grouped_elements])

    return unique_elements, repetitions

from itertools import groupby
X = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
%time x, num = np_encode(X)
print("Результат:")
print(x, num)
