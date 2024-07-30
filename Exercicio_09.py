# Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma
# média de 5 calorias por minuto de exercício.
dias = int(input('Entre com a quantidade de dias que você pratica exercícios fisicos: '))
horas = float(input('Entre com a quantidade de horas que você pratica exercícios fisicos: '))

minutos_por_dia = horas * 60
minutos_por_semana = minutos_por_dia *dias
calorias = 5

minutos_por_dia = horas * 60
minutos_por_semana = minutos_por_dia * dias

# Calorias queimadas por minuto
calorias_por_minuto = 5

# Calcule as calorias queimadas por semana e por mês
calorias_gastas_por_semana = calorias_por_minuto * minutos_por_semana
calorias_gastas_por_mes = calorias_gastas_por_semana * 4  # Aproximando para 4 semanas em um mês

print(f'Você gasta em média {calorias_gastas_por_mes:.2f} calorias por mês.')

