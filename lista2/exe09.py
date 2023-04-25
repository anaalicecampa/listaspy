salario_bruto = float(input("Digite o salário bruto: "))
proventos = float(input("Digite o valor dos proventos: "))

if salario_bruto <= 5000:
    desconto = salario_bruto * 0.05
else:
    desconto = salario_bruto * 0.1

salario_liquido = salario_bruto + proventos - desconto
print("O salário líquido é: R$", salario_liquido)
