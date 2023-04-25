while True:
    n = int(input("Digite um número inteiro positivo (menor que 16) para calcular o fatorial: "))
    if n < 0 or n > 15:
        print("Número inválido! O número deve ser um inteiro positivo menor que 16.")
        continue
    else:
        fatorial = 1
        for i in range(1, n+1):
            fatorial *= i
        print(f"{n}! = {fatorial}")
    opcao = input("Deseja calcular o fatorial de outro número? (S/N)").upper()
    if opcao == "N":
        break
