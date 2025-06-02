def find_residents():
    # Чтение входных данных
    with open('input2.txt', 'r') as f:
        n = int(f.readline())
        savings = list(map(float, f.readline().split()))

    # Создаем список кортежей (сбережения, идентификационный номер)
    # Идентификационные номера начинаются с 1
    residents = [(savings[i], i + 1) for i in range(n)]

    # Сортируем по сбережениям
    residents.sort()

    # Получаем нужные идентификационные номера
    poorest = residents[0][1]
    middle = residents[n // 2][1]
    richest = residents[-1][1]


    with open('output2.txt', 'w') as f:
        f.write(f"{poorest} {middle} {richest}\n")


if __name__ == "__main__":
    find_residents()