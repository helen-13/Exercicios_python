# Crie um dicionário representando um carrinho de compras.
# Adicione produtos (chaves) e quantidades (valores) ao carrinho.
# Calcule o total do carrinho de compra.

# Dicionário de produtos com preços
produtos = {
    'arroz': 6.50,
    'feijão': 8.50,
    'carne': 36.00,
    'farinha': 4.55,
    'leite': 7.00
}

# Dicionário para armazenar o carrinho de compras
carrinho = {}

# Loop para adicionar produtos ao carrinho
while True:
    nome = input('Digite o nome do produto para adicionar ao carrinho (ou "sair" para finalizar): ').strip().lower()
    
    if nome == "sair":
        break
    
    if nome in produtos:
        quantidade = int(input(f"Quantas unidades de {nome} você deseja adicionar? "))
        if nome in carrinho:
            carrinho[nome] += quantidade
        else:
            carrinho[nome] = quantidade
    else:
        print(f"Produto {nome} não encontrado.")

# Calcular o total do carrinho
total = 0
print("\nResumo do Carrinho:")
for produto, quantidade in carrinho.items():
    preco = produtos[produto]
    subtotal = preco * quantidade
    total += subtotal
    print(f"{produto.capitalize()}: {quantidade} x R${preco:.2f} = R${subtotal:.2f}")

print(f"\nTotal do carrinho: R${total:.2f}")

