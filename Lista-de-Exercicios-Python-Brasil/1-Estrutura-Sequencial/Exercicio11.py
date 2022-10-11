int_1 = int(input("Insira um número inteiro: "))
int_2 = int(input("Insira outro número inteiro: "))
real = float(input("Insira um número real: "))

a = (int_1 * 2) * (int_2 / 2)
b = (int_1 * 3) + real
c = real ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {a}")
print(f"A soma do triplo do primeiro com o terceiro: {b}")
print(f"O terceiro elevado ao cubo: {c}")
