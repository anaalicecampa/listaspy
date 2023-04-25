# Lendo as dimensões da matriz
linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

# Imprimindo a matriz
for i in range(linhas):
    for j in range(colunas):
        print("A{},{} ".format(i, j), end="")
    print("#")
