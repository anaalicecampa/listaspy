capacidade_maxima = int(input("Digite a capacidade máxima do restaurante: "))
clientes_chegaram = int(input("Digite a quantidade de clientes que chegaram: "))

if clientes_chegaram >= capacidade_maxima:
    print("Restaurante lotado, não há mais mesas disponíveis.")
else:
    print("Ainda há mesas disponíveis no restaurante.")
