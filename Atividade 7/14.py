alunos = []
aprovados = 0
exames = 0
reprovados = 0
soma_notas = 0

for i in range(6):
    nome = input("Digite o nome do aluno: ")
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))

    alunos.append(dict(nome=nome, nota1=n1, nota2=n2))
    #alunos.append({"nome": nome, "nota1": n1, "nota2": n2})


print(f"\nALUNO  -  1° PROVA  -  2° PROVA  -  MÉDIA  -  SITUAÇÃO")
for aluno in alunos:
    media = (aluno["nota1"] + aluno["nota2"]) / 2
    soma_notas = aluno["nota1"] + aluno["nota2"]
    situacao = ""

    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    elif media < 7 and media >= 5:
        situacao = "Exame"
        exames += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    print(f"{aluno["nome"]}     -   {aluno["nota1"]}      -  {aluno["nota2"]}      -     {media}    -    {situacao}")

media_classe = soma_notas / (len(alunos) * 2)

percentual_apr = (aprovados / len(alunos)) * 100
percentual_exa = (exames / len(alunos)) * 100
percentual_rep = (reprovados / len(alunos)) * 100

print("\nMédia da Classe = ", media_classe)
print("Percentual de Alunos Aprovados = ", percentual_apr)
print("Percentual de Alunos de Exame = ", percentual_exa)
print("Percentual de Alunos Reprovados = ", percentual_rep)