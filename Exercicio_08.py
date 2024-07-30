# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês.Calcule e mostre o total do seu
# salário no referido mês.

valor_hora = int(input('Entre com o valor da hora de trabalho: '))
horas_trabalhadas =int(input('Entre com valor de horas trabalhado: '))
dia_trabalhado = valor_hora * horas_trabalhadas
mes = 30*dia_trabalhado

salario = mes
print(f'Seu salário será: {salario} reais.')
