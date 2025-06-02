def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    # Чтение входных данных из файла
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    # Сортировка массива
    insertion_sort(arr)

    # Запись результата в файл
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, arr)) + '\n')


if __name__ == "__main__":
    main()