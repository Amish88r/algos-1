# Чтение из файла
with open('input.txt', 'r') as file:  # подняться на уровень выше
    a, b = map(int, file.readline().split())

# Вычисление суммы
result = a + b

# Запись результата в файл
with open('output.txt', 'w') as file:
    file.write(str(result))