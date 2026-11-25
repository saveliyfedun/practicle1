# Задача 8.1. Аналіз коливань цін на акції за допомогою ковзного вікна

prices = [120, 125, 118, 130, 135, 128, 140, 145]
k = 3  # розмір вікна (кількість днів)

# Рахуємо суму першого вікна
window_sum = sum(prices[:k])
max_sum = window_sum
min_sum = window_sum

# Зсуваємо вікно по списку
for i in range(k, len(prices)):
    window_sum = window_sum + prices[i] - prices[i - k]
    if window_sum > max_sum:
        max_sum = window_sum
    if window_sum < min_sum:
        min_sum = window_sum

print("Ціни на акції:", prices)
print(f"Максимальна середня ціна за {k} дні:", round(max_sum / k, 2))
print(f"Мінімальна середня ціна за {k} дні:", round(min_sum / k, 2))


print("-" * 40)


# Задача 8.2. Оптимізація перевірки енергоспоживання за префіксними сумами

energy = [15, 22, 18, 30, 25, 19, 27]  # споживання за кожну годину

# Будуємо масив префіксних сум
prefix = [0] * (len(energy) + 1)
for i in range(len(energy)):
    prefix[i + 1] = prefix[i] + energy[i]

# Запити на перевірку споживання за період з години L по годину R (індекси від 0)
queries = [(0, 2), (1, 4), (3, 6)]

print("Споживання по годинах:", energy)
for left, right in queries:
    period_sum = prefix[right + 1] - prefix[left]
    print(f"З {left} по {right} годину витрачено: {period_sum} кВт")