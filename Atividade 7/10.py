lista1 = []
lista2 = []

resultante1 = []
resultante2 = []

soma = 0

#Preenche os dois vetores iniciais
for i in range(10):
    entrada = int(input("Digite um número: "))
    lista1.append(entrada)
for i in range(5):
    entrada = int(input("Digite um número: "))
    lista2.append(entrada)

#Preenche o primeiro vetor resultante
for par in lista1:
#Verifica de 'par' realmente é par, preferi usar separado para ficar mais legível, mas poderia usar 'par' diretamente no lugar de 'soma'
    if par % 2 == 0:
        #Guarda em outra variável para ficar mais legível
        soma = par
        for idx, num in enumerate(lista2):
            soma += lista2[idx]
        resultante1.append(soma)

#Preenche o segundo vetor resultante
for impar in lista1:
    if impar % 2 != 0:
        qtd = 0
        #Verifica cada número da lista e se for divisível acumula na quantidade
        for num in lista2:
            
            if impar % num == 0:
                qtd += 1

        resultante2.append(qtd)

print("O primeiro vetor resultante é: ", resultante1)
print("O segundo vetor resultante é: ", resultante2)