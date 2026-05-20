lista = []

for i in range(15):
    entrada = int(input("Digite um valor:"))
    lista.append(entrada)


for idx, n in enumerate(lista):
    if n == 30:
        print("Aparece na posição: ", idx)