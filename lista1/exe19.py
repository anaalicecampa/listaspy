conta = input("Digite o número da conta corrente (3 dígitos): ")

# Verifica se a entrada tem 3 dígitos
if len(conta) != 3:
    print("Número de conta inválido. Digite um número com 3 dígitos.")
else:
    # Calcula o número invertido
    inverso = int(conta[::-1])
    
    # Calcula a soma da conta com seu inverso
    soma = int(conta) + inverso
    
    # Calcula o dígito verificador
    dv = str(soma)
    posicao = 1
    total = 0
    for d in dv:
        total += int(d) * posicao
        posicao += 1
    dv_conta = total % 10
    
    print(f"O dígito verificador da conta {conta} é {dv_conta}.")
