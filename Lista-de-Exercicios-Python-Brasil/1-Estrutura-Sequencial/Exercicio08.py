valor_hora = float(input("Insira o valor ganho por hora: "))
horas_trab = float(input("Insira o total de horas trabalhadas no mês: "))

salario = valor_hora * horas_trab

print(f"O seu salário é de R${salario:.2f}")
