salario_atual = float(input('Insira o salário atual do colaborador: '))

if salario_atual <= 280:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_do_aumento = (salario_atual / 100) * percentual_aumento
salario_novo = salario_atual + valor_do_aumento

print(f'O salário antes do reajuste era: R${salario_atual:.2f}\n'
    f'O percentual de aumento é de: {percentual_aumento}%\n'
    f'O valor do aumento é R${valor_do_aumento:.2f}\n'
    f'O novo salário após o aumento é: R${salario_novo:.2f}')
