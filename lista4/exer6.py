limite_inferior = float(input("Digite o limite inferior (em graus Celsius): "))
limite_superior = float(input("Digite o limite superior (em graus Celsius): "))
decremento = float(input("Digite o decremento: "))
print("Celsius\tFahrenheit")
while limite_inferior <= limite_superior:
    fahrenheit = limite_inferior * 9/5 + 32
    print(f"{limite_inferior:.1f}\t{fahrenheit:.1f}")
    limite_inferior += decremento