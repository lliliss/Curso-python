# if depende do else e vice-versa
# Aula de condições - python
# O if pode estar sozinho
# Checa até ver se uma condição é verddeira, se não for, vai pular

entrada = input("Você quer entrar (1) ou sair (2)? ")

if entrada == "1":
    print("Parabéns, você entrou no sistema!")

elif entrada == "2":
    print("Você se retirou do sistema!")
else:
    print("Erro no sistema, número não encontrado!")