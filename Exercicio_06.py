# Escreva um programa que calcule o tempo de uma viagem.
# Faça um comparativo do mesmo percurso de avião, carro e ônibus.
#  Levando em consideração:
#  ● avião = 600 km/h
#  ● carro = 100 km/h
#  ● ônibus = 80 km/h

# Função para calcular o tempo de viagem
def calcular_tempo_viagem(distancia, velocidade):
    return distancia / velocidade

# Distância do percurso (em km)
distancia = int(input('Entre com a distância em quilometro (Km): '))

# Calculando o tempo de viagem para cada meio de transporte
tempo_aviao = calcular_tempo_viagem(distancia, 600)
tempo_carro = calcular_tempo_viagem(distancia, 100)
tempo_onibus = calcular_tempo_viagem(distancia, 80)

# Exibindo os resultados
print("Tempo de viagem para um percurso de " + str(distancia) + " km:")
print("Avião: " + str(tempo_aviao) + " horas")
print("Carro: " + str(tempo_carro) + " horas")
print("Ônibus: " + str(tempo_onibus) + " horas")