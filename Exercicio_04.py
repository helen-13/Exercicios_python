# Crie um dicionário representando contatos (nome, telefone).
# Permita ao usuário procurar por um contato pelo nome.
# Dicionário para armazenar os contatos
contatos = {
    'Alice': '1234-5678',
    'Bob': '2345-6789',
    'Carol': '3456-7890',
    'Dave': '4567-8901',
    'Eve': '5678-9012'
}

# Solicita ao usuário o nome do contato para pesquisa
nome = input('Digite o nome do contato que você deseja procurar: ')

# Procura o contato pelo nome e exibe o telefone, se encontrado
if nome in contatos:
    print(f"O telefone de {nome} é: {contatos[nome]}")
else:
    print(f"Contato {nome} não encontrado.")

