limite = 500

# Inicializa os dois primeiros termos da série
fibonacci = [0, 1]

# Gera os próximos termos da série até que o último termo seja maior que o limite
while fibonacci[-1] < limite:
    termo_atual = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(termo_atual)

# Exibe a série de Fibonacci gerada
print("Série de Fibonacci:")
for termo in fibonacci:
    print(termo, end=" ")
