# Lendo dois números inteiros
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))

# Verificando se A é divisível por B
if a % b == 0:
    print(f"{a} é divisível por {b}.")
else:
    print(f"{a} não é divisível por {b}.")
