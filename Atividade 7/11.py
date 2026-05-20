lista = []
res1 = []
res2 = []

for i in range(10):
    entrada = int(input("Digite um numero: "))
    lista.append(entrada)

    if entrada % 2 == 0:
        res1.append(entrada)
    else:
        res2.append(entrada)

print("O vetor com os números pares é: ", res1)
print("O vetor com os números impares é: ", res2)