nomes = []
medias = []

for i in range(7):
    nome = input("Digite o nome do aluno: ")
    nomes.append(nome)

    media = float(input("Digite a média final desse aluno: "))
    medias.append(media)

for idx, media in enumerate(medias):
    recuperacao = 0
    if media == max(medias):
        print("O aluno com a maior média é: ", nomes[idx], " - ", media)
    elif media < 7:
        #Recuperação aplicada na media: (media + x) / 2 = 5 --> (5*2) - media = x
        recuperacao = (5*2) - media
        print(f"O aluno {nomes[idx]} ficou de recuperação. No exame final o aluno precisa tirar no mínimo {recuperacao}")
