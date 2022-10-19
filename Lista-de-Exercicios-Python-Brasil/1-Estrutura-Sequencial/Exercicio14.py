peso_peixes = float(input("Insira o peso dos peixes: "))

if peso_peixes >= 50:
    excesso = peso_peixes - 50
    multa = excesso * 4
    print(f"O peso excedente foi: {excesso:.3f}kg")
    print(f"O valor da multa é: R${multa:.2f}")
