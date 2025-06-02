def solve_queue_with_minimum(input_file="input3.txt", output_file="output3.txt"):
    """
    Решает задачу "Очередь с минимумом", считывая команды из input_file
    и записывая результаты в output_file.
    """
    queue = []
    output_lines = []

    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    if not lines:
        with open(output_file, 'w') as f_out:
            pass
        return

    try:
        m = int(lines[0])
        commands = [line.strip() for line in lines[1:]]
    except ValueError:
        with open(output_file, 'w') as f_out:
            f_out.write("Ошибка в формате входного файла.\n")
        return

    for command in commands:
        if command.startswith('+'):
            try:
                value = int(command[1:])
                queue.append(value)
            except ValueError:
                output_lines.append("Ошибка: некорректное значение для добавления.\n")
        elif command == '-':
            if queue:
                queue.pop(0)
            else:
                output_lines.append("Очередь пуста, операция удаления невозможна.\n")
        elif command == '?':
            if queue:
                output_lines.append(str(min(queue)) + '\n')
            else:
                output_lines.append("Очередь пуста, операция поиска минимума невозможна.\n")
        else:
            output_lines.append(f"Ошибка: неизвестная команда '{command}'.\n")

    with open(output_file, 'w') as f_out:
        f_out.writelines(output_lines)

if __name__ == "__main__":
    # Создаем пример файла input.txt (для тестирования)
    with open("input3.txt", 'w') as f:
        f.write("7\n")
        f.write("+ 1\n")
        f.write("?\n")
        f.write("- \n")
        f.write("+ 10\n")
        f.write("?\n")
        f.write("?\n")
        f.write("-\n")
        f.write("?\n")

    solve_queue_with_minimum()

    # Выводим содержимое output.txt (для проверки)
    with open("output3.txt", 'r') as f:
        print("Содержимое output.txt:")
        print(f.read())