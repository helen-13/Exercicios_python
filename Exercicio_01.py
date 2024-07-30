# Programa que pede dois números e realiza as operações básicas: 
# soma, subtração, multiplicação e divisão.
# Função para obter um número válido entre 0 e 10
def obter_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if 0 <= numero < 10:
                return numero
            else:
                print('Você errou, entre com um valor de 0 a 10.')
        except ValueError:
            print('Entrada inválida. Por favor, entre com um número inteiro.')

# Solicita os dois números
numero_1 = obter_numero('Entre com um número de 0 a 10: ')
numero_2 = obter_numero('Entre com outro número de 0 a 10: ')

# Realiza as operações
soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2 if numero_2 != 0 else 'Indefinida (divisão por zero)'

# Exibe os resultados
print('Os valores somados são: {}, a subtração dos valores é: {}, a multiplicação dos valores é: {} e a divisão dos valores é: {}'.format(soma, subtracao, multiplicacao, divisao))