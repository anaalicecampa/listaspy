n = int(input("Digite a quantidade de CDs da coleção: "))
total_investido = 0

for i in range(n):
    valor = float(input(f"Digite o valor do CD {i+1}: "))
    total_investido += valor

media_gasto = total_investido / n

print(f"O valor total investido na coleção é R$ {total_investido:.2f}")
print(f"A média gasta em cada CD é de R$ {media_gasto:.2f}")
