turno = input('Insira o turno em que você estuda:\n'
            'M - matutino\n'
            'V - vespertino\n'
            'N - Noturno\n')

turno = turno.upper()

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite')
else:
    print('Valor inválido!')
