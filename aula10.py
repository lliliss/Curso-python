# Fatiamento de strings e Função len
# O len conta caracteres da string q você tiver
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Qual a sua idade? ")

if nome and idade:
    print(f"Seu nome é {nome} e você tem {idade} anos.")
    print(f"O 'nome' {nome} invertido ficaria: {nome[::-1]}.")

    if " " in nome:
        print(f"Seu nome possui espaços.")
        #print(f"Ademais, seu nome possui {len(nome)} espaços.")
    else:
        print(f"Seu nome não possui espaços.")

    print(f"Seu nome possui: {len(nome)} letras, incluindo espaços.")
    print(f"A primeira letra do seu nome é:  {nome[0]}.")
    print(f"A última letra do seu nome é: {nome[-1]}.")

else:
    print("Erro! Possui campos vazios.")
