num_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado do polígono: "))

if num_lados == 3:
    perimetro = medida_lado * 3
    print("TRIANGULO")
    print(f"Perímetro: {perimetro}")
    
elif num_lados == 4:
    area = medida_lado ** 2
    print("QUADRADO")
    print(f"Área: {area}")
    
elif num_lados == 5:
    print("PENTAGONO")
    
elif num_lados < 3:
    print("Não é um polígono")
    
else:
    print("Polígono não identificado")
