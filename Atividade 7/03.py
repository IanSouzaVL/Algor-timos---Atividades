codigos = []
estoques = []

for i in range(10):
    entrada = int(input("Digite o codigo do produto que deseja cadastrar: "))
    codigos.append(entrada)
    entrada = int(input("Digite o estoque do produto que cadastrou: "))
    estoques.append(entrada)

print("\nCadastro de produtos finalizado! Iniciando fase de compra!\n")

while True:
    codigo = int(input("Digite o codigo do produto que deseja comprar: "))

    if codigo == 0:
        break
    else:
        if codigo in codigos:
            qtd = int(input("Digite a quantidade: "))

            if estoques[codigos.index(codigo)] >= qtd:
                estoques[codigos.index(codigo)] -= qtd
                print("Pedido atendido, obrigado e volte sempre!")
            else:
                print("Não temos estoque suficiente dessa mercadoria!")
        else:
            print("Código inexistente!")


for i in range(10):
    print("Codigo: ", codigos[i], " | Estoque: ", estoques[i])