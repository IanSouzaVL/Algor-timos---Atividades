lista = []
for i in range(1, 6):
    entrada = int(input(f"Digite o {i}° número: "))
    lista.append(entrada)

print("Os números digitados foram:", " + ".join(map(str, lista)), "=", sum(lista))