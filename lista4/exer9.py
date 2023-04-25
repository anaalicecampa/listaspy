branco = 0
nulo = 0
kiko = 0
chaves = 0
chiquinha = 0

while True:
    voto = int(input("Digite o número do seu candidato (ou 666 para encerrar a votação): "))
    if voto == 1:
        branco += 1
    elif voto == 2:
        nulo += 1
    elif voto == 3:
        kiko += 1
    elif voto == 4:
        chaves += 1
    elif voto == 5:
        chiquinha += 1
    elif voto == 666:
        break

print("Resultado da votação:")
print("Branco:", branco)
print("Nulo:", nulo)
print("Kiko:", kiko)
print("Chaves:", chaves)
print("Chiquinha:", chiquinha)