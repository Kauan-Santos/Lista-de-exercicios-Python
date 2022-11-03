letra = str(input("Insira uma letra: "))

letra = letra.upper()

if letra  in ["A", "E", "I", "O", "U"]:
    print("Esta letra é uma vogal!")
else:
    print("Esta letra é uma consoante!")
