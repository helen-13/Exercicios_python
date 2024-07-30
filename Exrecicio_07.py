# Solicite ao usuário o peso em kg e a altura em metros. Calcule e
# imprima o Índice de Massa Corporal (IMC) usando a fórmula:
#  IMC = peso / (altura x altura).
peso = float(input('Entre com o valor do seu peso quilograma (kg): '))
altura = float(input('Entre com o valor do seu altura usando ponto para separa(m): '))

imc = peso/(altura**2)

print(f'Seu IMC é de:{imc:.2f}') 