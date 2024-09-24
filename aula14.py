"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

'''user = int(input("Digite um número: "))

if user % 2 == 0:
    print("O número é par.")
elif user % 2 != 0:
    print("O número é ímpar.")
else:
    print("O que o usuário digitou não é um número, ou não é um número inteiro.")'''


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

'''horario = int(input("Digite um horário inteiro: "))

if horario >= 0 and horario <= 11:
    print("Bom dia!")
elif horario >= 12 and horario <= 17:
    print("Boa tarde!")
elif horario >= 18 and horario <= 23:
    print("Boa noite!")
else:
    print("O digitado não é um horário.")'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = str(input("Digite seu nome: "))
letras = len(nome)

if letras <= 4:
    print("Seu nome é curto.")
elif letras >= 5 and letras <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é gigante!")