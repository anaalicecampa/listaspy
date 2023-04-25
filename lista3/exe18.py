num = int(input("Digite um número inteiro: "))

divisores = []
for i in range(1, num+1):
    if num % i == 0:
        divisores.append(i)

if len(divisores) == 2:
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo e é divisível por {divisores}.")
