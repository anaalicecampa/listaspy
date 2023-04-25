n = int(input("Digite a quantidade de termos: "))

s = 0.0
for i in range(1, n+1):
    s += i/(i+1)

print(f"O valor de S para {n} termos é {s:.2f}")