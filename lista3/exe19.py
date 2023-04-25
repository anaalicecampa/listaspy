n = int(input("Digite um número inteiro: "))

primo = True
cont_divisoes = 0

for i in range(2, n+1):
    primo = True
    for j in range(2, i):
        cont_divisoes += 1
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)

print(f"O número de divisões realizadas foi: {cont_divisoes}")
