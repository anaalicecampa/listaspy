num_turmas = int(input("Digite o número de turmas: "))
total_alunos = 0
for i in range(num_turmas):
    while True:
        num_alunos = int(input(f"Digite o número de alunos da turma {i+1}: "))
        if num_alunos <= 40:
            total_alunos += num_alunos
            break
        else:
            print("A turma não pode ter mais de 40 alunos.")
media_alunos = total_alunos / num_turmas
print(f"A média de alunos por turma é {media_alunos:.2f}.")
