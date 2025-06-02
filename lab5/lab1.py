import sys
from collections import deque


def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    with open(input_filename, 'r') as f:
        lines = f.readlines()

    if not lines:
        with open(output_filename, 'w') as f:
            pass
        return

    S, n = map(int, lines[0].split())
    packets = []
    for line in lines[1:n + 1]:
        if line.strip():
            Ai, Pi = map(int, line.split())
            packets.append((Ai, Pi))

    buffer = deque()
    output = []

    for Ai, Pi in packets:
        # Удаляем из буфера пакеты, обработка которых завершилась к моменту Ai
        while buffer and buffer[0] <= Ai:
            buffer.popleft()

        if len(buffer) >= S:
            output.append(-1)
        else:
            if not buffer:
                start_time = Ai
            else:
                start_time = buffer[-1]
            finish_time = start_time + Pi
            buffer.append(finish_time)
            output.append(start_time)

    with open(output_filename, 'w') as f:
        for result in output:
            f.write(f"{result}\n")


if __name__ == "__main__":
    main()