# Faça um Programa que peça as quatro notas de 5 alunos, calcule
# e armazene numa lista a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.

# Lista para armazenar as médias dos alunos
medias = []

# Lista de nomes dos alunos
alunos = ['Helen', 'Esther', 'Elias', 'Luiz', 'Ana']

# Loop para coletar dados de cada aluno
for aluno in alunos:
    print(f"Aluno {aluno}:")
    notas = []  # Lista para armazenar as notas de um aluno

    # Coletar as quatro notas do aluno
    for j in range(4):
        nota = float(input(f"Entre com a nota {j + 1}: "))
        notas.append(nota)

    # Calcular a média do aluno e adicionar à lista de médias
    media = sum(notas) / len(notas)
    medias.append(media)

# Contar quantos alunos têm média maior ou igual a 7.0
alunos_acima_de_7 = sum(1 for media in medias if media >= 7.0)

# Imprimir o resultado
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_acima_de_7}")