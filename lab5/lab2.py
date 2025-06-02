import heapq


def solve():
    with open('input2.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        tasks = list(map(int, f.readline().split()))

    # Инициализация кучи: все потоки доступны в момент времени 0
    heap = []
    for i in range(n):
        heapq.heappush(heap, (0, i))

    results = []
    for time_needed in tasks:
        # Извлекаем поток, который освободится раньше всех
        available_time, thread_idx = heapq.heappop(heap)
        start_time = max(available_time, 0)
        results.append((thread_idx, start_time))
        # Обновляем время освобождения потока
        heapq.heappush(heap, (start_time + time_needed, thread_idx))

    with open('output2.txt', 'w') as f:
        for thread_idx, start_time in results:
            f.write(f"{thread_idx} {start_time}\n")


solve()