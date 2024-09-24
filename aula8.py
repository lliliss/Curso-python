'''
Interpolação básica de strings
s - string / %s
d e i - int / %d ou %i
f - float / %f
x e x - hexadecimal - ABCDEFGH0123456 / %x
'''
nome = "Alice"
preco = 250.925
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %x" % (150, 15))