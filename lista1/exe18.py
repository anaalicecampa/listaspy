 # Entrada de dados
quantidade_fitas = int(input("Digite a quantidade de fitas da locadora: "))
valor_aluguel = float(input("Digite o valor do aluguel de cada fita: "))

# Cálculo do faturamento anual
faturamento_anual = (quantidade_fitas / 3) * 12 * valor_aluguel

# Cálculo do valor ganho com multas por mês
quantidade_alugueis_mes = quantidade_fitas / 3
quantidade_devolucoes_atraso = quantidade_alugueis_mes / 10
valor_multas_mes = quantidade_devolucoes_atraso * valor_aluguel * 0.1

# Cálculo da quantidade de fitas no final do ano
quantidade_fitas_estragadas = quantidade_fitas * 0.02
quantidade_fitas_compradas = quantidade_fitas / 10
quantidade_final = quantidade_fitas - quantidade_fitas_estragadas + quantidade_fitas_compradas

# Saída de dados
print("Faturamento anual: R$ {:.2f}".format(faturamento_anual))
print("Valor ganho com multas por mês: R$ {:.2f}".format(valor_multas_mes))
print("Quantidade de fitas no final do ano: {}".format(int(quantidade_final)))
