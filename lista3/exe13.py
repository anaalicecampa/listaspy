numero = int(input("Digite um número inteiro: "))

# Inicializa o fatorial como 1
fatorial = 1

# Calcula o fatorial do número
for i in range(1, numero+1):
    fatorial *= i

# Exibe o resultado
print(f"{numero}! = {fatorial}")
