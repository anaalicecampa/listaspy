a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# Variável auxiliar para armazenar o valor de A antes da troca
aux = a

# Efetua a troca dos valores de A e B
a = b
b = aux

print("Valores trocados: A =", a, "e B =", b)
