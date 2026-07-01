nums = []
seqs = []
seq = 0
maior = 0
for _ in range(8):
    num = int(input("Digite um número: "))
    nums.append(num)

for idx in range(8):
    if idx == 7:
        seq += 1
        seqs.append(seq)
        seq = 0
    elif nums[idx] < nums[idx + 1]:
        seq += 1
    else:
        seq += 1
        seqs.append(seq)
        seq = 0

for i in range(len(seqs)):
    if i == (len(seqs) - 1):
        pass
    elif seqs[i] > seqs[i + 1]:
        maior = seqs[i]
    else:
        maior = seqs[i + 1]

print(f"Números digitados: {nums}")
print(f"Maior sequência crescente consecutiva: {maior}")