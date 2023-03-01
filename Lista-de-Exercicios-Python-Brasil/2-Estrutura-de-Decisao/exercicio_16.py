"Exercicio 16"
from math import sqrt

a = float(input("Insira o valor de A: "))

if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Insira o valor de B: "))
    c = float(input("Insira o valor de C: "))

    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        raiz = -b / (2 * a)
        print("A equação possui apenas uma raiz real: ", raiz)
    else:
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b - sqrt(delta)) / (2 * a)
        print("A equação possui duas raízes reais: ", raiz1, " e ", raiz2)
