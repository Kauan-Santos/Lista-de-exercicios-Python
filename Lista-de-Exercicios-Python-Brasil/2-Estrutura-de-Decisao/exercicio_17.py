"Exercicio 17"

ano = int(input("Informe um ano para consultar se é ou não bissexto: "))

resultado = ano % 4

if resultado == 0:
    print("Este ano é bissexto!")
else:
    print("Este ano não é bissexto!")
