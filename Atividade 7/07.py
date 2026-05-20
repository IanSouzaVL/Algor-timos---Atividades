numeros = []
negativos = 0
soma_positivos = 0
for i in range(10):
    num = float(input("Digite um número: "))
    numeros.append(num)

for num in numeros:
    if num < 0:
        negativos += 1
    else:
        soma_positivos += num

print("O total de númeors negativos é: ", negativos)
print("A soma dos positivos é: ", soma_positivos)