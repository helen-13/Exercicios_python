#Faça um Programa que peça a quantidade de quilômetros, transforme
#  em metros, centímetros e milímetros.
def valor_transformacao_km(valor_km):
    centimetro = valor_km*100000
    metro = valor_km*1000
    milimetro = valor_km*1000000
    return centimetro, metro, milimetro

valor_km = int(input('Entre com a quilometragem desejada em Km: '))
centimetro, metro, milimetro = valor_transformacao_km(valor_km)
print(f'O valor{valor_km} transformado em centimetro{centimetro: ,}, metro {metro:,} e milimetro: {milimetro:,}')