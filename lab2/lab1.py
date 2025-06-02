import time
import random

def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
    return n, arr

def write_output(arr, filename="output.txt"):
    with open(filename, "w") as f:
        f.write(" ".join(map(str, arr)))

def generate_test_cases():
    test_cases = []
    # Worst case: reverse sorted
    test_cases.append(list(range(1000, 0, -1)))
    test_cases.append(list(range(10000, 0, -1)))
    test_cases.append(list(range(100000, 0, -1)))

    # Best case: already sorted
    test_cases.append(list(range(1000)))
    test_cases.append(list(range(10000)))
    test_cases.append(list(range(100000)))

    # Average case: random numbers
    test_cases.append([random.randint(1, 1000) for _ in range(1000)])
    test_cases.append([random.randint(1, 10000) for _ in range(10000)])
    test_cases.append([random.randint(1, 100000) for _ in range(100000)])
    return test_cases

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    # Задача 1: Сортировка слиянием
    n_from_file, arr_from_file = read_input()
    start_time = time.time()
    sorted_arr = merge_sort(arr_from_file)
    end_time = time.time()
    sorting_time = end_time - start_time
    print(f"Сортировка слиянием массива из файла заняла: {sorting_time:.4f} сек.")
    write_output(sorted_arr)
    print("Отсортированный массив записан в output.txt")

    # Задача 2: Анализ производительности
    print("\nАнализ производительности:")
    test_cases = generate_test_cases()
    for i, case in enumerate(test_cases):
        size = len(case)
        case_type = ""
        if all(case[j] >= case[j + 1] for j in range(len(case) - 1)):
            case_type = "худший случай (обратно отсортированный)"
        elif all(case[j] <= case[j + 1] for j in range(len(case) - 1)):
            case_type = "лучший случай (уже отсортированный)"
        else:
            case_type = "средний случай (случайные числа)"

        # Merge Sort
        start_time = time.time()
        merge_sort(list(case)) # Сортируем копию, чтобы не изменять исходный тест-кейс
        merge_sort_time = time.time() - start_time

        # Insertion Sort
        start_time = time.time()
        insertion_sort(list(case)) # Сортируем копию
        insertion_sort_time = time.time() - start_time

        print(f"\nТест {i+1}: Размер массива = {size}, {case_type}")
        print(f"  Время сортировки слиянием: {merge_sort_time:.4f} сек.")
        print(f"  Время сортировки вставкой: {insertion_sort_time:.4f} сек.")

    # Задача 3: Реализация Merge без сигнальных значений
    # Реализация уже выполнена в функции merge()
    # Границы p, r и q используются в стандартной рекурсивной реализации Merge Sort,
    # которая уже реализована в функции merge_sort().
    print("\nЗадача 3: Реализация Merge без сигнальных значений")
    print("Реализация Merge без сигнальных значений и с использованием индексов уже выполнена в функции merge().")
    print("Функция merge_sort() использует стандартный подход с определением границ подмассивов.")