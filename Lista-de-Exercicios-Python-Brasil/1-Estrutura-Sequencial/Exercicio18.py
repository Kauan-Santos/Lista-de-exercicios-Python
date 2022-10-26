tamanho_do_arquivo = int(input("Insira o tamanho do arquivo para download em MB: "))
velocidade_do_link = int(input("Insira a velocidade do link de internet: "))

tempo = (tamanho_do_arquivo / velocidade_do_link) / 60

print(f"Irá demorar {tempo:.0f} minutos")
