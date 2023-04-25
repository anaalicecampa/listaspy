n = int(input("Informe a quantidade de pessoas: "))

soma_idades = 0
for i in range(n):
    idade = int(input("Informe a idade da pessoa {}: ".format(i+1)))
    soma_idades += idade

media_idades = soma_idades / n

if media_idades <= 25:
    print("A média de idade da turma é de {:.1f} anos. A turma é jovem.".format(media_idades))
elif media_idades <= 60:
    print("A média de idade da turma é de {:.1f} anos. A turma é adulta.".format(media_idades))
else:
    print("A média de idade da turma é de {:.1f} anos. A turma é idosa.".format(media_idades))
