import datetime

def find_max_crossing_subarray(arr, low, mid, high):
    """
    Находит максимальный подмассив, пересекающий середину.
    """
    max_left_sum = float('-inf')
    current_sum = 0
    max_left_index = mid
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > max_left_sum:
            max_left_sum = current_sum
            max_left_index = i

    max_right_sum = float('-inf')
    current_sum = 0
    max_right_index = mid + 1
    for j in range(mid + 1, high + 1):
        current_sum += arr[j]
        if current_sum > max_right_sum:
            max_right_sum = current_sum
            max_right_index = j

    return max_left_index, max_right_index, max_left_sum + max_right_sum

def find_maximum_subarray(arr, low, high):
    """
    Находит максимальный непрерывный подмассив, используя подход "разделяй и властвуй".
    """
    if high == low:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def parse_stock_data(filename="input2.txt"):
    """
    Читает данные об акциях из файла и возвращает список изменений цен.
    Предполагается, что каждая строка файла содержит дату и цену акции, разделенные запятой.
    Например: 2023-10-26,150.20
    """
    dates = []
    prices = []
    try:
        with open(filename, "r") as f:
            for line in f:
                date_str, price_str = line.strip().split(',')
                dates.append(datetime.datetime.strptime(date_str, '%Y-%m-%d').date())
                prices.append(float(price_str))
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return [], []
    except ValueError:
        print("Ошибка: Неверный формат данных в файле.")
        return [], []

    if not prices or len(prices) < 2:
        print("Недостаточно данных для анализа.")
        return [], []

    price_changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
    return dates[1:], price_changes, prices

def write_output(filename="output2.txt", company_name="Неизвестная компания", buy_date=None, sell_date=None, buy_price=None, sell_price=None, max_profit=None):
    """
    Записывает результаты анализа в выходной файл.
    """
    with open(filename, "w") as f:
        f.write(f"Анализ акций компании: {company_name}\n")
        if buy_date and sell_date and max_profit is not None:
            f.write(f"Дата покупки: {buy_date}\n")
            f.write(f"Дата продажи: {sell_date}\n")
            f.write(f"Цена покупки за акцию: {buy_price:.2f}\n")
            f.write(f"Цена продажи за акцию: {sell_price:.2f}\n")
            f.write(f"Максимальная прибыль за акцию: {max_profit:.2f}\n")
        else:
            f.write("Не удалось определить оптимальные даты покупки и продажи.\n")

if __name__ == "__main__":
    company_name = "Примерная компания"  # Замените на название вашей компании

    # Шаг 1: Получение данных об акциях
    all_dates, price_changes, all_prices = parse_stock_data()

    if price_changes:
        # Шаг 2: Применение алгоритма поиска максимального подмассива к изменениям цен
        if price_changes:
            low, high, max_profit_change = find_maximum_subarray(price_changes, 0, len(price_changes) - 1)

            # Шаг 3: Определение дат покупки и продажи
            if max_profit_change > 0:
                buy_date = all_dates[low]
                sell_date = all_dates[high]
                buy_price = all_prices[low]
                sell_price = all_prices[high + 1] # +1, так как изменения цен на один день меньше, чем сами цены
                max_profit = sell_price - buy_price
            else:
                buy_date = None
                sell_date = None
                buy_price = None
                sell_price = None
                max_profit = 0 # Если нет положительной прибыли, считаем ее 0

            # Шаг 4: Запись результатов в выходной файл
            write_output(company_name=company_name, buy_date=buy_date, sell_date=sell_date, buy_price=buy_price, sell_price=sell_price, max_profit=max_profit)
            print(f"Анализ завершен. Результаты записаны в файл output.txt")
        else:
            print("Нет изменений цен для анализа.")
    else:
        print("Не удалось получить данные об акциях.")