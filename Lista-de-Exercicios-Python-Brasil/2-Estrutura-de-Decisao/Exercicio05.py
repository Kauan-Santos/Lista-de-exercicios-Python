nota_1 = float(input("Insira a 1ª nota do aluno: "))
nota_2 = float(input("Insira a 2ª nota do aluno: "))

media = (nota_1 + nota_2) / 2

if media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Aprovado")
