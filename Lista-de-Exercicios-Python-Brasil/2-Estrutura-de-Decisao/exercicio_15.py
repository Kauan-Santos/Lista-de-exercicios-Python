"Exercicio 15"
print("Informe 3 lados de um triângulo: ")
lado_1 = float(input("Lado 1: "))
lado_2 = float(input("Lado 2: "))
lado_3 = float(input("Lado 3: "))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    if lado_1 == lado_2 and lado_2 == lado_3:
        print("Triângulo equilátero")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("Triângulo Isósceles")
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")
