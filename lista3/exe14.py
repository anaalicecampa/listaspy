N = int(input("Digite a quantidade de números a serem inseridos: "))

# Inicializa as variáveis menor, maior e soma com valores iniciais
# que garantem que qualquer número digitado pelo usuário será menor ou maior que elas
menor = float("inf")
maior = float("-inf")
soma = 0

# Lê os N números digitados pelo usuário e atualiza as variáveis menor, maior e soma
for i in range(N):
    numero = float(input(f"Digite o {i+1}º número: "))
    menor = min(menor, numero)
    maior = max(maior, numero)
    soma += numero

# Exibe os resultados
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
