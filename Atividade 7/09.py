produtos = []
codigos = []
precos = []
aumento = 0
valorFinal = 0

for i in range(1, 4):
    entrada = input(f"Digite o nome do {i}° produto: ")
    produtos.append(entrada)
    entrada = int(input(f"Digite o código: "))
    codigos.append(entrada)
    entrada = float(input(f"Digite o preço: "))
    precos.append(entrada)
    print()

print("Relatório\n")
for idx, produto in enumerate(produtos):
    if (codigos[idx] % 2 == 0) and (precos[idx] > 1000.00):
        aumento = precos[idx] * 0.20
    elif codigos[idx] % 2 == 0:
        aumento = precos[idx] * 0.15
    elif precos[idx] > 1000.00:
        aumento = precos[idx] * 0.10
    else:
        aumento = 0
    
    valorFinal = precos[idx] + aumento

    print(f"Nome do Produto - {produtos[idx]}\nCodigo - {codigos[idx]}\nPreco - {precos[idx]}\nNovo Preço - {valorFinal}\n")
