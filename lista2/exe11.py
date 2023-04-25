dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verifica se o mês está entre 1 e 12
if mes < 1 or mes > 12:
    print("Data inválida.")
else:
    # Define a quantidade de dias de cada mês, considerando os anos bissextos
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verifica se o dia está dentro do intervalo do mês
    if dia < 1 or dia > dias_por_mes[mes-1]:
        print("Data inválida.")
    else:
        print("Data válida.")
