import numpy as np

def np_diag_2k(a):
    # Получаем диагональные элементы
    diag_elements = np.diag(a)
    
    # Выбираем только четные элементы
    even_diag_elements = diag_elements[diag_elements % 2 == 0]
    
    # Если есть четные элементы, возвращаем их сумму, иначе возвращаем 0
    return even_diag_elements.sum() if len(even_diag_elements) > 0 else 0

# Задаем квадратную матрицу
a = np.random.randint(1, 10, size=(5, 5))
print("Матрица:")
print(a)

# Засекаем время работы функции с NumPy
result = np_diag_2k(a)
print(f"Сумма четных диагональных элементов: {result}")
