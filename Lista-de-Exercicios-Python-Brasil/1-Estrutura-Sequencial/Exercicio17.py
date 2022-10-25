area_a_pintar = float(input("Insira a área (em m2) a ser pintada: "))

litros = area_a_pintar / 6
litros_com_folga = litros * 1.1

latas = litros // 18 + 1
valor_total_latas = latas * 80
print(f"Opção 1 - latas de 18 litros: necessário {latas:.0f} lata(s) de 18 litros. O valor total é: R${valor_total_latas:.2f}")

galoes = litros // 3.6 + 1
valor_total_galoes = galoes * 25
print(f"Opção 2 - galoes de 3,6 litros: necessário {galoes:.0f} galao(oes) de 3,6 litros. O valor total é: R${valor_total_galoes:.2f}")

latas_misto = litros_com_folga // 18
litros_faltantes = litros_com_folga % 18
galoes_misto = (litros_faltantes // 3.6) + 1
valor_total = (latas_misto * 80) + (galoes_misto * 25)

print(f"Opção 3 - A quantidade de latas para comprar é {latas_misto:.0f} e galões é {galoes_misto:.0f} (margem 10%) - Valor: R$ {valor_total:.2f}")
