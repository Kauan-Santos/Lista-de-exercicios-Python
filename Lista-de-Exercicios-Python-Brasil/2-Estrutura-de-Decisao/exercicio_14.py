"Exercicio 14"
nota_1 = float(input("Insira a primeira nota do aluno: "))
nota_2 = float(input("Insira a primeira nota do aluno: "))

media = (nota_1 + nota_2) / 2

if media > 9:
    CONCEITO = "A - APROVADO"
elif media > 7.5:
    CONCEITO = "B - APROVADO"
elif media > 6:
    CONCEITO = "C - APROVADO"
elif media > 4:
    CONCEITO = "D - REPROVADO"
else:
    CONCEITO = "E - REPROVADO"

print(f"Nota 1: {nota_1}\n"
    f"Nota 2: {nota_2}\n"
    f"Média: {media}\n"
    f"Conceito: {CONCEITO}")
