valor_hora = float(input('Insira o valor ganho por hora: '))
horas_trabalhadas_no_mes = float(input('Insira a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_trabalhadas_no_mes

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2

sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
total_descontos = ir + sindicato
salario_liquido = salario_bruto - total_descontos

print(
    f'\nSalário Bruto: ({horas_trabalhadas_no_mes} * {valor_hora:.2f})     : R$ {salario_bruto:.2f}\n'
    f'(-) IR (5%)                       : R$ {ir:.2f}\n'
    f'(-) SINDICATO (3%)                : R$ {sindicato:.2f}\n'
    f'FGTS (11%)                        : R$ {fgts:.2f}\n'
    f'Total de descontos                : R$ {total_descontos:.2f}\n'
    f'Salário Líquido                   : R$ {salario_liquido:.2f}'
)
