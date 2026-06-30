start = True
produtos = []

def cadastro():
    for i in range(5):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))

        produtos.append({
            'nome': nome,
            'preco': preco
        })

def listar50():
    qtd = 0
    print("Produtos com preços abaixo de 50,00\n")
    for produto in produtos:
        if produto['preco'] < 50:
            print(f"{produto['nome']}: {produto['preco']}")
            qtd += 1
    if qtd > 0:
        print(f"Quantidade: {qtd}")
    else:
        print("Nenhum produto foi encontrado :(")


def listar50_a_100():
    print("Produtos com preços entre de 50,00 e 100,00\n")
    qtd = 0
    for produto in produtos:
        if produto['preco'] >= 50 and produto['preco'] < 100:
            qtd += 1
            print(f"Nome: {produto['nome']} (R$ {produto['preco']})")
    if qtd == 0:
        print("Nenhum produto foi encontrado :(")

def listar100():
    print("Média dos produtos com preços acima de 100\n")

    total = 0
    qtd = 0
    
    for produto in produtos:
        if produto['preco'] > 100:
            qtd += 1
            total += produto['preco']
    if qtd != 0:
        media = total/qtd
        print(f"Média: {media}")
    else:
        print("Nenhum produto com preço acima de 100,00 foi encontrado :(")

while start:
    entrada = '0'
    if len(produtos) > 0:
        print("Menu\n\n1 - Cadastro de Produtos\n2 - Preços inferiores à 50,00\n3 - Preços entre 50,00 e 100,00\n4 - Média dos produtos com preços acima de 100,00\n\nDigite 'sair' para sair")
        entrada = input("Escolha uma opção: ")
    else:
        cadastro()
    
    if entrada == '1':
        cadastro()
    elif entrada == '2':
        listar50()
    elif entrada == '3':
        listar50_a_100()
    elif entrada == '4':
        listar100()
    elif entrada == "sair":
        print("Fechando programa...")
        start = False