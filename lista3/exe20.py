n = int(input("Digite a quantidade de notas: "))
soma = 0

for i in range(n):
    nota = float(input("Digite a nota {}: ".format(i+1)))
    soma += nota

media = soma / n

print("A média aritmética das {} notas é {:.2f}".format(n, media))
