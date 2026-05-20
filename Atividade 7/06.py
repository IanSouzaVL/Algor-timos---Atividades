vendas = []
nomes = []
comissoes = []

for i in range(2):
    nome = input("Digite o nome do vendedor: ")
    nomes.append(nome)
    
    total_vendas = float(input("Digite o o valor total vendido: "))
    vendas.append(total_vendas)

    comissao = float(input("Digite o percentual de comissão (ex:para 10% escreva 10, para 5% escreva 5): "))
    comissoes.append((comissao/100) * total_vendas)


print("Relatório\n")
n = 1
for idx, nome in enumerate(nomes):
    print(f"{n}° Funcionário")
    print(f"Nome - {nome}")
    print(f"Comissão à receber - {comissoes[idx]}\n")
    n += 1

