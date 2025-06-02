def swap_sort():
    # Чтение входных данных
    with open('input3.txt', 'r') as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    # Открываем выходной файл для записи
    with open('output3.txt', 'w') as f:
        # Реализация сортировки выбором с записью перестановок
        for i in range(n - 1):
            # Находим индекс минимального элемента в оставшейся части
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            # Если нашли элемент меньше текущего, делаем перестановку
            if min_idx != i:
                # Записываем перестановку
                f.write(f"Swap elements at indices {i + 1} and {min_idx + 1}.\n")
                # Выполняем перестановку
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Записываем завершающую фразу
        f.write("No more swaps needed.\n")


if __name__ == "__main__":
    swap_sort()