nota = float(input())
while nota != -1:
    notas = float(input())
    notas.append(nota)
    i+=1

media = sum(notas) / len(notas)

if media >= 7:
    print("Aluno aprovado com nota:", media)
else:
    print("Aluno reprovado com nota:", media)
