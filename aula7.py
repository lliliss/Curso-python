# OR - avalia toda condição verdadeira em verdadeira
# Avaliação de curto circuito.

# Not utilizado para inverter a expressão, o que é False vira True e  vice-versa.

# Operadores "In" (estar entre) e "Not in" (não estar entre)

#Ex de como funciona para procurar tal letra doo nome:
'''0 1 2 3 4
A l i c e
-5 -4 -3 -2 -1 '''
#Ex not in e in:
#nome = "Alice"
#print(nome[2])
nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")