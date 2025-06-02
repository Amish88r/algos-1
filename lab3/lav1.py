import random
import sys
import time

def randomized_partition(arr, low, high):
    """
    Выбирает случайный опорный элемент и разбивает массив.

    Args:
        arr (list): Список для разбиения.
        low (int): Нижняя граница подмассива.
        high (int): Верхняя граница подмассива.

    Returns:
        int: Индекс опорного элемента после разбиения.
    """
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high)

def partition(arr, low, high):
    """
    Разбивает подмассив относительно последнего элемента (опорного).

    Args:
        arr (list): Список для разбиения.
        low (int): Нижняя граница подмассива.
        high (int): Верхняя граница подмассива.

    Returns:
        int: Индекс опорного элемента после разбиения.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    """
    Реализация алгоритма быстрой сортировки с случайным выбором опорного элемента.

    Args:
        arr (list): Список для сортировки.
        low (int): Нижняя граница подмассива.
        high (int): Верхняя граница подмассива.
    """
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

def read_input(filename="input.txt"):
    """
    Считывает входные данные из файла.

    Args:
        filename (str): Имя входного файла.

    Returns:
        list: Список целых чисел, прочитанных из файла.
    """
    with open(filename, "r") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
    return arr

def write_output(arr, filename="output.txt"):
    """
    Записывает отсортированный массив в файл.

    Args:
        arr (list): Отсортированный массив.
        filename (str): Имя выходного файла.
    """
    with open(filename, "w") as f:
        f.write(" ".join(map(str, arr)))

if __name__ == "__main__":
    # Чтение входных данных
    input_array = read_input()
    n = len(input_array)

    # Сортировка с использованием Randomized-QuickSort
    start_time = time.time()
    randomized_quicksort(input_array, 0, n - 1)
    end_time = time.time()
    sorting_time = end_time - start_time

    # Запись отсортированного массива в выходной файл
    write_output(input_array)

    print(f"Массив из {n} элементов успешно отсортирован.")
    print(f"Время сортировки: {sorting_time:.4f} сек.")

    # Дополнительная проверка (генерация и сортировка случайных массивов для анализа)
    print("\nДополнительная проверка:")
    test_cases = [
        (10**3, 10**9, True),  # Наихудший случай (обратно отсортированный)
        (10**3, 10**9, False), # Лучший случай (уже отсортированный)
        (10**3, 10**9, None),  # Средний случай (случайный)
        (10**4, 10**9, None),
        (10**5, 10**9, None),
    ]

    for size, max_val, reversed_sort in test_cases:
        arr_test = [random.randint(1, max_val) for _ in range(size)]
        if reversed_sort is True:
            arr_test.sort(reverse=True)
            case_type = "худшем"
        elif reversed_sort is False:
            arr_test.sort()
            case_type = "лучшем"
        else:
            case_type = "среднем"

        arr_copy_randomized = arr_test[:]
        start_time_randomized = time.time()
        randomized_quicksort(arr_copy_randomized, 0, len(arr_copy_randomized) - 1)
        end_time_randomized = time.time()
        time_randomized = end_time_randomized - start_time_randomized

        arr_copy_standard = arr_test[:]
        start_time_standard = time.time()
        arr_copy_standard.sort() # Стандартная сортировка Python для сравнения
        end_time_standard = time.time()
        time_standard = end_time_standard - start_time_standard

        print(f"\nСортировка массива из {size} элементов (случай {case_type}):")
        print(f"  Randomized-QuickSort: {time_randomized:.4f} сек.")
        print(f"  Стандартная sort():    {time_standard:.4f} сек.")

    print("\nДля более детального сравнения с Median-QuickSort и Tail-Recursive-QuickSort, обратитесь к заданию 10.2 и Кормену и др., 2013, стр. 217.")