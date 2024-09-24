# Aula de como definir variável e receber dados via input além de imprimi-los.

nome = input("Digite seu nome: ")
altura = input("Digite sua altura: ")
peso = input("Digite seu peso: ")
altura_1 = float(altura)
imc = peso / (altura_1 ** 2)
print(f"{nome}", "tem", f"{altura}", "de altura", "pesa", f"{peso}", "kg", "e seu imc é de", f"{imc: .2f}")