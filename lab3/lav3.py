import math

def distance_to_origin(point):
    """Вычисляет евклидово расстояние точки от начала координат (0, 0)."""
    return math.sqrt(point[0]**2 + point[1]**2)

def find_k_closest_points(n, k, points):
    """Находит k ближайших точек к началу координат."""
    distances = [(distance_to_origin(point), point) for point in points]
    distances.sort(key=lambda item: item[0])  # Сортировка по расстоянию
    return [point for dist, point in distances[:k]]  # Возвращаем k ближайших точек

if __name__ == "__main__":
    try:
        with open('input3.txt', 'r') as infile:
            first_line = infile.readline().strip().split()
            n = int(first_line[0])
            k = int(first_line[1])
            points = []
            for _ in range(n):
                line = infile.readline().strip().split()
                x = int(line[0])
                y = int(line[1])
                points.append([x, y])

        closest_k = find_k_closest_points(n, k, points)
        output = ",".join([f"[{p[0]},{p[1]}]" for p in closest_k])  # Форматируем вывод

        with open('output3.txt', 'w') as outfile:
            outfile.write(output)

    except FileNotFoundError:
        print("Error: Input file 'input.txt' not found.")
    except ValueError:
        print("Error: Invalid input format in 'input.txt'.")
    except Exception as e:
        print(f"An error occurred: {e}")