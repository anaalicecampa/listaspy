while True:
    nota = float(input("Digite uma nota de 0 a 10: "))
    if nota >= 0 and nota <= 10:
        break
    else:
        print("Valor inválido. Digite novamente.")

print("Nota válida: ", nota)
