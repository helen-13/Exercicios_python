#Faça um programa que permita ao usuário digitar o seu nome e
# em seguida mostre o nome do usuário de trás para frente
# utilizando somente letras maiúsculas. Dica: lembre−se que ao
# informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input('Digite o seu nome: ').upper()

# Reverter a string
nome_revertido = nome[::-1]

# Exibir o nome revertido
print(f"Nome de trás para frente: {nome_revertido}")

