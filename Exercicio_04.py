#Receba do usuário a quantidade de litros de combustível consumidos e
# a distância percorrida. Calcule e imprima o consumo médio em km/l.
def calcular_consumo_medio(distancia, combustivel):
    return distancia / combustivel

# Definindo valores fixos
km_percorrida = int(input('Entre com o valor percorrido: '))  
quantidade_combustivel = int(input('Entre com o total de combustível: '))  

consumo_medio = calcular_consumo_medio(km_percorrida, quantidade_combustivel)
print(f'Você gastou em média: {consumo_medio:.2f} km/l de combustível')