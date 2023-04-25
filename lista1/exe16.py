valor = float(input("Digite o valor da prestação em atraso: "))
taxa = float(input("Digite a taxa de juros ao mês (%): "))
tempo = int(input("Digite o tempo de atraso em meses: "))

prestacao = valor + (valor * (taxa/100) * tempo)

print("O valor da prestação em atraso é de: R$", prestacao)
