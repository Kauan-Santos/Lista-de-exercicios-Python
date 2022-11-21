numeros = []

numeros.append(input("Insira o 1º numero: "))
numeros.append(input("Insira o 2º numero: "))
numeros.append(input("Insira o 3º numero: "))

numeros = sorted(numeros, reverse=True)

for numero in numeros:
    print(numero, end=" ")
