num = int(input("Digite um número inteiro: "))

# Verifica se o número é 1 ou negativo
if num <= 1:
    print(f"{num} não é um número primo.")
    exit()

# Verifica se o número é divisível por algum número entre 2 e sua metade
for i in range(2, num//2 + 1):
    if num % i == 0:
        print(f"{num} não é um número primo.")
        break
else:
    print(f"{num} é um número primo.")
