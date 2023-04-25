limite_superior = float(input("Digite o limite superior do intervalo em Fahrenheit: "))
incremento = float(input("Digite o incremento em Fahrenheit: "))
limite_inferior = 10

print("Tabela de conversão de Fahrenheit para Celsius:")
print("Fahrenheit \t Celsius")
fahrenheit = limite_inferior
while fahrenheit <= limite_superior:
    celsius = (fahrenheit - 32) * 5/9
    print("{:.2f} \t\t {:.2f}".format(fahrenheit, celsius))
    fahrenheit += incremento
