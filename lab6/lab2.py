import math


def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x


def is_fibonacci_number(num):
    if num == 1:
        return True
    x = 5 * num * num + 4
    y = 5 * num * num - 4
    return is_perfect_square(x) or is_perfect_square(y)


def main():
    # Чтение из файла input.txt
    with open('input2.txt', 'r') as f:
        lines = f.read().splitlines()

    N = int(lines[0])
    numbers = lines[1:N + 1]  # Берём следующие N чисел

    results = []
    for num_str in numbers:
        num = int(num_str)
        if is_fibonacci_number(num):
            results.append("Yes")
        else:
            results.append("No")

    # Запись в файл output.txt
    with open('output2.txt', 'w') as f:
        f.write('\n'.join(results))


if __name__ == "__main__":
    main()