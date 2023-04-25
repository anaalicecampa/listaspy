salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatts = float(input("Digite a quantidade de quilowatts consumidos: "))

valor_quilowatt = salario_minimo/700
valor_pagar = valor_quilowatt * quilowatts
valor_desconto = valor_pagar * 0.1
novo_valor = valor_pagar - valor_desconto

print("Valor em reais de cada quilowatt:", valor_quilowatt)
print("Valor em reais a ser pago:", valor_pagar)
print("Novo valor a ser pago com desconto de 10%:", novo_valor)
