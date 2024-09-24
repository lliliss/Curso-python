#Variáveis, constantes e complexidade.

velocidade = int(input("Insira a velocidade do carrro: ")) #Velocidade em que o carro se encontra.
quilometragem = int(input("Qual km ele está? ")) #Limite de km na estrada em que o carro se encontra.

RADAR_1 = 90 #Velocidade máx. do radar 1.
KM_1 = 110 #Local onde o radar 1 está.
RADAR_RANGE = 1 #Distância onde o radar pega.

if velocidade > RADAR_1:
    print("Velocidade maior que o radar.")

elif quilometragem >= (KM_1 - RADAR_RANGE) and \
        quilometragem <= (KM_1 + RADAR_RANGE) and \
            velocidade > RADAR_1:
    print("Carro mutado no radar.")

else:
    print("Carro passou do radar.")