numbers = input("Введите числа через пробел: ").split()


if all(numbers[0] == num for num in numbers):
    print("Все числа равны")

elif len(numbers) == len(set(numbers)):
    print("Все числа разные")

else:
    print("Есть равные и неравные числа")
