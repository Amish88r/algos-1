import time
import numpy as np

def multiply_naive(X, Y):
    """
    Наивное умножение матриц.
    """
    n = len(X)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def strassen_multiply(X, Y):
    """
    Умножение матриц методом Штрассена.
    Предполагает, что размеры матриц являются степенью 2.
    """
    n = len(X)
    if n == 1:
        return [[X[0][0] * Y[0][0]]]

    # Разбиение матриц на подматрицы
    mid = n // 2
    A = [row[:mid] for row in X[:mid]]
    B = [row[mid:] for row in X[:mid]]
    C = [row[:mid] for row in X[mid:]]
    D = [row[mid:] for row in X[mid:]]
    E = [row[:mid] for row in Y[:mid]]
    F = [row[mid:] for row in Y[:mid]]
    G = [row[:mid] for row in Y[mid:]]
    H = [row[mid:] for row in Y[mid:]]

    # Вычисление семи матриц произведения
    P1 = strassen_multiply(A, subtract_matrices(F, H))
    P2 = strassen_multiply(add_matrices(A, B), H)
    P3 = strassen_multiply(add_matrices(C, D), E)
    P4 = strassen_multiply(D, subtract_matrices(G, E))
    P5 = strassen_multiply(add_matrices(A, D), add_matrices(E, H))
    P6 = strassen_multiply(subtract_matrices(B, D), add_matrices(G, H))
    P7 = strassen_multiply(subtract_matrices(A, C), add_matrices(E, F))

    # Вычисление блоков результирующей матрицы
    R = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    S = add_matrices(P1, P2)
    T = add_matrices(P3, P4)
    U = subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)

    # Сборка результирующей матрицы
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        result[i][:mid] = R[i]
        result[i][mid:] = S[i]
        result[mid + i][:mid] = T[i]
        result[mid + i][mid:] = U[i]
    return result

def add_matrices(A, B):
    """
    Сложение двух матриц.
    """
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

def subtract_matrices(A, B):
    """
    Вычитание двух матриц.
    """
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]
    return result

def read_input(filename="input3.txt"):
    """
    Читает две квадратные матрицы A и B из входного файла.
    Первая строка содержит размер матриц n.
    Следующие n строк содержат элементы матрицы A, разделенные пробелами.
    Затем следуют n строк с элементами матрицы B, также разделенные пробелами.
    """
    try:
        with open(filename, "r") as f:
            n = int(f.readline())
            matrix_a = []
            for _ in range(n):
                matrix_a.append(list(map(int, f.readline().split())))
            matrix_b = []
            for _ in range(n):
                matrix_b.append(list(map(int, f.readline().split())))
            return matrix_a, matrix_b
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None, None
    except ValueError:
        print("Ошибка: Неверный формат данных во входном файле.")
        return None, None

def write_output(filename="output3.txt", result_matrix=None):
    """
    Записывает результирующую матрицу C = A * B в выходной файл.
    """
    if result_matrix is None:
        print("Нет результирующей матрицы для записи.")
        return

    with open(filename, "w") as f:
        n = len(result_matrix)
        for i in range(n):
            f.write(" ".join(map(str, result_matrix[i])) + "\n")
    print(f"Результат умножения матриц записан в файл '{filename}'")

def pad_matrix(matrix):
    """
    Дополняет матрицу нулями до ближайшей степени 2.
    """
    n = len(matrix)
    if n & (n - 1) == 0:  # n is a power of 2
        return matrix
    else:
        next_power_of_2 = 1
        while next_power_of_2 < n:
            next_power_of_2 *= 2
        padded_matrix = [row + [0] * (next_power_of_2 - n) for row in matrix]
        for _ in range(next_power_of_2 - n):
            padded_matrix.append([0] * next_power_of_2)
        return padded_matrix

def unpad_matrix(matrix, original_size):
    """
    Удаляет дополнение из матрицы до исходного размера.
    """
    return [row[:original_size] for row in matrix[:original_size]]

if __name__ == "__main__":
    matrix_a, matrix_b = read_input()

    if matrix_a and matrix_b:
        n_original = len(matrix_a)

        # Убедимся, что матрицы квадратные и одного размера
        if len(matrix_a) != len(matrix_a[0]) or len(matrix_b) != len(matrix_b[0]) or len(matrix_a) != len(matrix_b):
            print("Ошибка: Входные матрицы должны быть квадратными и одного размера.")
        else:
            n = len(matrix_a)

            # Наивное умножение
            start_time = time.time()
            result_naive = multiply_naive(matrix_a, matrix_b)
            end_time = time.time()
            naive_time = end_time - start_time
            print(f"Время наивного умножения: {naive_time:.4f} сек.")

            # Умножение Штрассена
            padded_a = pad_matrix(matrix_a)
            padded_b = pad_matrix(matrix_b)
            n_padded = len(padded_a)

            start_time = time.time()
            result_strassen_padded = strassen_multiply(padded_a, padded_b)
            result_strassen = unpad_matrix(result_strassen_padded, n_original)
            end_time = time.time()
            strassen_time = end_time - start_time
            print(f"Время умножения методом Штрассена: {strassen_time:.4f} сек.")

            # Вывод результата Штрассена в файл
            write_output(result_matrix=result_strassen)