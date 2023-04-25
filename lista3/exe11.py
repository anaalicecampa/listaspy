n = int(input("Digite o valor de n para gerar a série de Fibonacci: "))

# Inicializa os dois primeiros termos da série
fibonacci = [1, 1]

# Gera os próximos termos da série até n
for i in range(2, n):
    termo_atual = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(termo_atual)

# Exibe a série de Fibonacci gerada
print("Série de Fibonacci:")
for termo in fibonacci:
    print(termo, end=" ")
