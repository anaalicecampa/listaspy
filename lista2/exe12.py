codigo = int(input("Digite o código do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

maior_nota = max(nota1, nota2, nota3)

media = (4 * maior_nota + 3 * (nota1 + nota2 + nota3 - maior_nota)) / 10

print("Código do aluno: ", codigo)
print("Notas: ", nota1, nota2, nota3)
print("Média: ", media)

if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO")
