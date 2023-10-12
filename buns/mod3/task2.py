n = input().strip()
print(f"{int(n):b}, {int(n):o}, {int(n):X}" if n.isdigit() else "Неверный ввод")
