import sys


def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        n = int(infile.readline().strip())
        elements = set()
        output = []

        for _ in range(n):
            parts = infile.readline().strip().split()
            if not parts:
                continue
            op = parts[0]
            if len(parts) < 2:
                continue  # некорректная строка, пропускаем
            x = int(parts[1])

            if op == 'A':
                elements.add(x)
            elif op == 'D':
                if x in elements:
                    elements.remove(x)
            elif op == '?':
                if x in elements:
                    output.append('Y')
                else:
                    output.append('N')

        outfile.write(' '.join(output) + '\n')


if __name__ == "__main__":
    main()