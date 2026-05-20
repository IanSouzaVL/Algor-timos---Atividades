alunos = []
soma_notas = 0
for i in range(1, 3):
    nome = input(f"Digite o nome do(a) {i}° aluno: ")
    nota = float(input(f"Digite a nota do(a) {nome}: "))
    #alunos.append(dict(nome=nome, nota=nota))
    alunos.append({"nome": nome, "nota": nota})

print("\nRelatório de Notas")

for aluno in alunos:
    print(aluno["nome"], aluno["nota"])
    soma_notas += aluno["nota"]

media = soma_notas/len(alunos)

print("Média da classe = ", media)