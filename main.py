# Задача 9.1. Декомпозиція системи аналізу студентських оцінок


def get_average(grades):
  return sum(grades) / len(grades)


def get_grade_letter(avg):
  if avg >= 90:
    return "A"
  elif avg >= 75:
    return "B"
  elif avg >= 60:
    return "C"
  else:
    return "F"


def show_result(name, grades):
  avg = get_average(grades)
  letter = get_grade_letter(avg)
  print(f"{name}: середній бал = {avg:.1f}, оцінка = {letter}")


show_result("Олег", [85, 90, 78])
show_result("Анна", [95, 92, 98])
show_result("Максим", [55, 60, 50])


print("-" * 30)


# Задача 9.2. Валідація та конвертація валют із контрактом (Preconditions)


def convert_usd_to_uah(amount, rate):
  # Контракт (передумови): сума і курс мають бути більші за 0
  assert amount > 0, "Сума має бути більшою за 0"
  assert rate > 0, "Курс має бути більшим за 0"

  return round(amount * rate, 2)


money = float(input("Введіть суму в доларах: "))
course = 41.5

result = convert_usd_to_uah(money, course)
print("Сума в гривнях:", result)