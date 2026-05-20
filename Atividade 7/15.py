clientes = []
locacoes = []
locacoes_gratis = []

for i in range(2):
    nome = input("Digite o nome do cliente: ")
    qtd = int(input("Digite a quantidade de locações do cliente: "))
    clientes.append(nome)
    locacoes.append(qtd)

    gratis = 0

    while 10 <= qtd:
        if qtd - 10 >= 0:
            qtd -= 10
            gratis += 1
    locacoes_gratis.append(gratis)

for idx, nome in enumerate(clientes):
    print("Nome - ", nome)
    print("Locações - ", locacoes[idx])
    print("Locações Grátis - ", locacoes_gratis[idx], "\n")
