numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero2 == 0:
    print("Impossível dividir", numero1, "por zero!")
else:
    resultado = numero1 / numero2
    print(numero1, "dividido por", numero2, "é igual a", resultado)
