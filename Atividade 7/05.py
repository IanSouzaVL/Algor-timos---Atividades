logica = []
lp = []
n = 0

print("Cadastro de alunos de Lógica\n")
for i in range(15):
    matricula = int(input("Digite a matrícula do aluno: "))
    logica.append(matricula)

print("Cadastro de alunos de Linguagem de Programação\n")
for i in range(10):
    matricula = int(input("Digite a matrícula do aluno: "))
    lp.append(matricula)

for mat in logica:
    if mat in lp:
        n += 1
    
print("O número de matrículas que aparecem nos dois vetores é: ", n)