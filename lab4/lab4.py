def solve_problem(input_filename="input4.txt", output_filename="output4.txt"):
    """
    Решает задачу о новобранцах, обрабатывая команды из входного файла
    и записывая результат в выходной файл.
    """
    try:
        with open(input_filename, "r") as infile:
            first_line = infile.readline().strip().split()
            n = int(first_line[0])
            m = int(first_line[1])
            initial_line = [None] * n
            for i in range(m):
                command_line = infile.readline().strip().split()
                rookie_index = int(command_line[0]) - 1
                command = command_line[1]

                if command == "left":
                    initial_line[rookie_index] = "L"
                elif command == "right":
                    initial_line[rookie_index] = "R"
                elif command == "leave":
                    initial_line[rookie_index] = "X"

            final_line = list(initial_line)
            for i in range(n):
                if initial_line[i] == "L":
                    j = i - 1
                    while j >= 0 and final_line[j] is None:
                        final_line[j] = "L"
                        j -= 1
                elif initial_line[i] == "R":
                    j = i + 1
                    while j < n and final_line[j] is None:
                        final_line[j] = "R"
                        j += 1

            first_occupied = -1
            last_occupied = -1
            occupied_count = 0
            for i in range(n):
                if final_line[i] is not None:
                    occupied_count += 1
                    if first_occupied == -1:
                        first_occupied = i
                    last_occupied = i

            output_string = ""
            if occupied_count > 0:
                output_string = f"{first_occupied + 1} {last_occupied + 1}"

            with open(output_filename, "w") as outfile:
                outfile.write(output_string)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден.")
    except ValueError:
        print("Ошибка: Некорректный формат входных данных.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    solve_problem()