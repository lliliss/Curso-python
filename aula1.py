'''nome = str("Alice")
sobrenome = str("Ferreira Correia")
idade = 19
ano_nascimento = str("30 de dezembro de 2003")
maior_de_idade = idade >= 18
altura_metros = str("1.67")

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura:", altura_metros)'''

nome = "Alice Ferreira"
altura = 1.67
peso = 90
imc = peso / (altura ** 2)
print(f"{nome}", "tem", f"{altura}", "de altura", "pesa", f"{peso}", "kg", "e seu imc é de", f"{imc: .2f}")