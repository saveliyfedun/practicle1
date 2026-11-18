# Задача 6.1. Посимвольний аналіз рядка за ASCII (без методів .is*())

text = input("Введіть рядок: ")

upper_count = 0
lower_count = 0
digits_count = 0
spaces_count = 0
others_count = 0

for char in text:
  code = ord(char)
  if 65 <= code <= 90:  # Великі літери A-Z
    upper_count += 1
  elif 97 <= code <= 122:  # Малі літери a-z
    lower_count += 1
  elif 48 <= code <= 57:  # Цифри 0-9
    digits_count += 1
  elif code == 32:  # Пробіл
    spaces_count += 1
  else:  # Інші символи
    others_count += 1

print("Великих літер:", upper_count)
print("Малих літер:", lower_count)
print("Цифр:", digits_count)
print("Пробілів:", spaces_count)
print("Інших символів:", others_count)


print("-" * 30)


# Задача 6.2. Перевірка на паліндром без урахування регістру через ASCII

text = input("Введіть рядок для перевірки на паліндром: ")
clean_text = ""

for char in text:
  code = ord(char)
  # Якщо велика літера (A-Z), переводимо в малу (+32 за таблицею ASCII)
  if 65 <= code <= 90:
    clean_text += chr(code + 32)
  # Якщо вже мала літера (a-z) або цифра (0-9) - залишаємо як є
  elif (97 <= code <= 122) or (48 <= code <= 57):
    clean_text += char

# Перевіряємо чи однаковий рядок зліва направо і справа наліво
if clean_text == clean_text[::-1]:
  print("Це паліндром")
else:
  print("Це не паліндром")