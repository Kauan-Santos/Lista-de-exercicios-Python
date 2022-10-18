h = float(input("Insira a altura da pessoa: "))

homens = (72.7 * h) - 58
mulheres = (62.1 * h) - 44.7

print("Peso ideal:")
print(f"a. Para homens: {homens:.1f}kg")
print(f"b. Para mulheres: {mulheres:.1f}kg")
