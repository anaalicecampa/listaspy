# leitura dos dados
id_aluno = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
me = float(input("Digite a média dos exercícios: "))

# cálculo da média de aproveitamento
ma = (nota1 + nota2*2 + nota3*3 + me) / 7

# cálculo do conceito
if ma >= 9:
    conceito = "A"
elif 7.5 <= ma < 9:
    conceito = "B"
elif 6 <= ma < 7.5:
    conceito = "C"
elif 4 <= ma < 6:
    conceito = "D"
else:
    conceito = "E"

# impressão dos resultados
print(f"Aluno: {id_aluno}")
print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Nota 3: {nota3:.1f}")
print(f"Média dos exercícios: {me:.1f}")
print(f"Média de aproveitamento: {ma:.1f}")
print(f"Conceito: {conceito}")

# verificação da situação do aluno
if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")
