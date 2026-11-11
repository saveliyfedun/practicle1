#2.1
binary_str = "1101"

decimal_value = 0
for bit in binary_str:
    decimal_value = decimal_value * 2 + int(bit)

print(decimal_value)



#2.2
n = 456

d3 = n % 10
d2 = (n // 10) % 10
d1 = n // 100

reversed_n = d3 * 100 + d2 * 10 + d1

print(reversed_n)