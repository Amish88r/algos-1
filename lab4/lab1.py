def solve():
    try:
        with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
            num_commands = int(infile.readline())
            stack = []
            output_numbers = []

            for _ in range(num_commands):
                line = infile.readline().strip()
                if not line:
                    continue  # Пропускаем пустые строки (на всякий случай)

                if line.startswith('+'):
                    value = int(line.split()[1])
                    stack.append(value)
                elif line == '-':
                    output_numbers.append(stack.pop())

            outfile.write("\n".join(map(str, output_numbers)) + "\n")

    except FileNotFoundError:
        print("Error: input.txt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    solve()