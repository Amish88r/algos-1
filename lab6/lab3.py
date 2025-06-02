def main():
    with open('input3.txt', 'r') as f:
        first_line = f.readline().strip().split()
        N, X, A, B = map(int, first_line)
        second_line = f.readline().strip().split()
        Ac, Bc, Ap, Bp = map(int, second_line)

    hash_table = set()

    for _ in range(N):
        if X in hash_table:
            A = (A + Ac) % 1000
            B = (B + Bc) % (10 ** 15)
        else:
            hash_table.add(X)
            A = (A + Ap) % 1000
            B = (B + Bp) % (10 ** 15)
        X = (X * A + B) % (10 ** 15)

    with open('output3.txt', 'w') as f:
        f.write(f"{X} {A} {B}\n")


if __name__ == "__main__":
    main()