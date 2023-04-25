idade = int(input("Digite a idade: "))

if idade >= 1 and idade <= 13:
    print("Criança")
elif idade > 13 and idade <= 20:
    print("Adolescente")
elif idade > 20 and idade <= 50:
    print("Adulto")
elif idade > 50:
    print("Idoso")
else:
    print("Idade inválida. Digite uma idade maior que 0.")
