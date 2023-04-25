while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    print("O nome deve ter mais de 3 caracteres.")

while True:
    idade = int(input("Digite sua idade (entre 0 e 150): "))
    if idade >= 0 and idade <= 150:
        break
    print("A idade deve estar entre 0 e 150 anos.")

while True:
    salario = float(input("Digite seu salário (maior que zero): "))
    if salario > 0:
        break
    print("O salário deve ser maior que zero.")

while True:
    sexo = input("Digite seu sexo (f/m): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    print("O sexo deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    print("O estado civil deve ser 's', 'c', 'v' ou 'd'.")

print("Nome: ", nome)
print("Idade: ", idade)
print("Salário: ", salario)
print("Sexo: ", sexo)
print("Estado civil: ", estado_civil)