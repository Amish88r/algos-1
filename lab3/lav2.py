def solve():
    with open('input2.txt', 'r') as f:
        n, k = map(int, f.readline().split())
        sizes = list(map(int, f.readline().split()))

    sorted_sizes = sorted(sizes)

    for i in range(k):  # Разбиваем на k независимых групп
        group = sizes[i::k]  # Элементы с шагом k, начиная с i
        group_sorted = sorted(group)

        # Заменяем элементы в исходном массиве на отсортированные
        pos = i
        for num in group_sorted:
            if num != sorted_sizes[pos]:
                with open('output2.txt', 'w') as f:
                    f.write("НЕТ")
                return
            pos += k

    with open('output2.txt', 'w') as f:
        f.write("ДА")


if __name__ == "__main__":
    solve()