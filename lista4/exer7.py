altura_aprico = 1.10
altura_josber = 1.50
anos = 0
while altura_aprico <= altura_josber:
    print(f"Apricoçildo: {altura_aprico:.2f}m, Josberanilson: {altura_josber:.2f}m")
    altura_aprico += 0.03
    altura_josber += 0.02
    anos += 1
print(f"Apricoçildo ultrapassa Josberanilson em {anos} anos.")