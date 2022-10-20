valor_hora = float(input("Insira o valor recebido por hora: "))
horas_mes = float(input("Insira o total de horas trabalhadas no mês: "))

salario_bruto = horas_mes * valor_hora
ir = (salario_bruto / 100) * 11
inss = (salario_bruto / 100) * 8
sindicato = (salario_bruto / 100) * 5
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"+ Salário Bruto: R${salario_bruto}\n"
      f"- IR (11%) : R${ir}\n"
      f"- INSS (8%) : R${inss}\n"
      f"- Sindicato (5%) : R${sindicato}\n"
      f"= Salário Liquido : R${salario_liquido}")
