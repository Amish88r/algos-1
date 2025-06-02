def main():
    import sys
    sys.setrecursionlimit(1000000)

    with open('input.txt', 'r') as f:
        n = int(f.read())

    if n == 1:
        with open('output.txt', 'w') as f:
            f.write('0\n1')
        return

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    sequence = []
    current = n
    while current >= 1:
        sequence.append(current)
        if current == 1:
            break
        candidates = [(current - 1, dp[current - 1])]
        if current % 2 == 0:
            candidates.append((current // 2, dp[current // 2]))
        if current % 3 == 0:
            candidates.append((current // 3, dp[current // 3]))
        current = min(candidates, key=lambda x: x[1])[0]

    sequence.reverse()

    with open('output.txt', 'w') as f:
        f.write(f"{len(sequence) - 1}\n")
        f.write(' '.join(map(str, sequence)))


if __name__ == "__main__":
    main()