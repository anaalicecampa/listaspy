num_eleitores = int(input("Digite o número total de eleitores: "))

votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0

for i in range(num_eleitores):
    print(f"Eleitor {i+1}, vote em um dos candidatos abaixo:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    
    voto = int(input("Digite o número do seu candidato: "))
    
    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        votos_candidato_3 += 1
    else:
        print("Opção inválida. Voto não computado.")

print(f"Resultado final da eleição:")
print(f"Candidato 1: {votos_candidato_1} votos")
print(f"Candidato 2: {votos_candidato_2} votos")
print(f"Candidato 3: {votos_candidato_3} votos")
