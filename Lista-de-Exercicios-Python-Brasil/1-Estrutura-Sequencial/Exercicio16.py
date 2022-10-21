area_a_ser_pintada = float(input("Insira a área em metros quadrados a ser pintada: "))

litros_utilizados = area_a_ser_pintada / 3

latas = int(litros_utilizados / 18 + 1)

preco = latas * 80.00

print(f"Latas a serem compradas: {latas}\n"
      f"Preço total: R${preco:.2f}")
