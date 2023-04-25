idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
  print("O nadador está na categoria Infantil A")
elif idade >= 8 and idade <= 10:
  print("O nadador está na categoria Infantil B")
elif idade >= 11 and idade <= 13:
  print("O nadador está na categoria Juvenil A")
elif idade >= 14 and idade <= 17:
  print("O nadador está na categoria Juvenil B")
elif idade >= 18:
  print("O nadador está na categoria Sênior")
else:
  print("Idade inválida!")
