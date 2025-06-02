# Чтение из файла input.txt
with open('input1.txt', 'r') as file:
    a, b = map(int, file.readline().split())

# Вычисление результата a + b²
result = a + b ** 2

# Запись результата в файл output.txt
with open('output1.txt', 'w') as file:
    file.write(str(result))