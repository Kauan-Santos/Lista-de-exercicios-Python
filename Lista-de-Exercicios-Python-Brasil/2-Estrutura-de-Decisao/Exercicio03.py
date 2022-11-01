letra = str(input("Informe o sexo (F/M): "))

letra = letra.upper()

if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo inválido")
