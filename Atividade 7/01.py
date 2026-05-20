lista = []
pares = []
impares = []

for _ in range(6):
    entrada = int(input("Digite um valor: "))
    lista.append(entrada)

    if (entrada % 2) == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)


print("\nOs pares são: ")
for _ in pares:
    print(_)

print("\nOs impares são: ")
for _ in impares:
    print(_)

print(f"O total de pares é: {len(pares)}\nO total de impares é: {len(impares)}")