numbers = [12, 5, 8, 20, 3, 15]

if not numbers:
    print("Список порожній")
else:
    minimum = numbers[0]
    maximum = numbers[0]
    total_sum = 0
    count = 0

    for num in numbers:
        total_sum = total_sum + num
        count = count + 1

        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    average = total_sum / count

    print("Кількість елементів:", count)
    print("Сума:", total_sum)
    print("Мінімум:", minimum)
    print("Максимум:", maximum)
    print("Середнє значення:", average)

print("-" * 25)

items = [1, 2, 3, 4, 5, 6]

left = 0
right = len(items) - 1

while left < right:
    temp = items[left]
    items[left] = items[right]
    items[right] = temp

    left = left + 1
    right = right - 1

print("Перевернутий список:", items)