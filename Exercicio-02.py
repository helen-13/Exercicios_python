#Peça ao usuário para informar o ano de nascimento. Em seguida,
# calcule e imprima a idade atual.
import datetime

# Função para calcular a idade
def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

# Definindo o ano de nascimento diretamente
ano_nascimento = int(input('Entre com o seu ano de nascimento:'))
idade = calcular_idade(ano_nascimento)

print('Você tem ' + str(idade) + ' anos de idade.')

# Adicionar uma mensagem personalizada com base na idade
if idade < 18:
    print('Você é menor de idade.')
elif 18 <= idade < 60:
    print('Você é um adulto.')
else:
    print('Você é um idoso.')

print('Programa concluído.')