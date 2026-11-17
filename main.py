# Задача 4.1. Ролі та права доступу (бітові маски)

READ = 1      # 0001
WRITE = 2     # 0010
DELETE = 4    # 0100
ADMIN = 8     # 1000

# Ролі
GUEST = READ
EDITOR = READ | WRITE
FULL_ADMIN = READ | WRITE | DELETE | ADMIN

user = GUEST
print("Початкові права:", bin(user))

# Додати право
user = user | WRITE
print("Додали WRITE:", bin(user))

# Перевірити право
has_write = (user & WRITE) == WRITE
has_admin = (user & ADMIN) == ADMIN
print("Є право WRITE:", has_write)
print("Є право ADMIN:", has_admin)

# Забрати право
user = user & ~WRITE
print("Забрали WRITE:", bin(user))

# Перемкнути право (якщо було - забере, якщо не було - дасть)
user = user ^ DELETE
print("Перемкнули DELETE:", bin(user))


print("-" * 30)


# Задача 4.2. Бітовий аналіз числа (без if та циклів)

num = int(input("Введіть ціле число: "))

# 1. Парність (1 - непарне, 0 - парне)
is_odd = bool(num & 1)

# 2. Знак числа (для 32-бітного числа: 1 - від'ємне, 0 - додатне)
is_negative = bool((num >> 31) & 1)

# 3. Модуль числа без if
mask = num >> 31
abs_num = (num + mask) ^ mask

# 4. Чи є число степенем двійки (наприклад 2, 4, 8, 16...)
is_pow2 = (num > 0) and ((num & (num - 1)) == 0)

# 5. Молодший встановлений біт (крайня права одиниця)
lowest_bit = num & -num

# 6. Кількість одиниць у двійковому записі
ones_count = num.bit_count()

print("Двійковий вигляд:", bin(num))
print("Непарне:", is_odd)
print("Від'ємне:", is_negative)
print("Модуль числа:", abs_num)
print("Степінь двійки:", is_pow2)
print("Молодший біт:", lowest_bit)
print("Кількість одиниць:", ones_count)