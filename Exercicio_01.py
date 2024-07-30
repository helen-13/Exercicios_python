# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#  As perguntas são:
# ""Telefonou para a vítima?""
# ""Esteve no local do crime?""
#""Mora perto da vítima?""
#""Devia para a vítima?""
#""Já trabalhou com a vítima?""
#O programa deve no final emitir uma classificação sobre a participação
#  da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
# ""Assassino"".Caso contrário,ele será classificado como""Inocente"".

# Lista de perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Inicializa o contador de respostas positivas
respostas_positivas = 0

# Loop para fazer as perguntas e coletar respostas
for pergunta in perguntas:
    resposta = input(pergunta + " (s/n): ").strip().lower()
    if resposta == 's':
        respostas_positivas += 1

# Classificação baseada nas respostas
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Exibe a classificação final
print(f"A pessoa foi classificada como: {classificacao}")
