lista = []
m2 = []
m3 = []
m2e3 = []

for i in range(7):
    entrada = int(input("Digite um valor: "))
    lista.append(entrada)

    if entrada % 2 == 0:
        m2.append(entrada)
    if entrada % 3 == 0:
        m3.append(entrada)
    if (entrada % 2 == 0) and (entrada % 3 ==0):
        m2e3.append(entrada)

print("Os multiplos de 2 são: ", m2)
print("Os multiplos de 3 são: ", m3)
print("Os multiplos de 2 e 3 são: ", m2e3)