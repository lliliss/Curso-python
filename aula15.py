# Tipos de imutáveis: float, bool, int, string, .
# Aula 15 sobre while (enquanto), laço de repetição. Enquanto uma condição for verdadeira, while continuará rodando.
''' Operações de atribuição:
+= / *= / -= / = / = ** = / %= /'''


'''contador = 0

while contador < 10:
    contador += 1
    print(contador)

print("Finalizou!")'''

# While + while (laço interno)

qntlinhas = 5
qntcolunas = 5

linha = 1
while linha <= qntlinhas:
    coluna = 1
    while coluna <= qntcolunas:
        print(f"{linha=} {coluna=}")
        coluna += 1
    linha += 1

print("Acabou.")