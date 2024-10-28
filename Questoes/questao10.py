frase = input("Digite uma frase:")

numero_vogais = 0
for letra in frase:
    if letra == "a" or letra == "A":
        numero_vogais += 1
    if letra == "e" or letra == "E":
        numero_vogais += 1
    if letra == "i" or letra == "I":
        numero_vogais += 1
    if letra == "o" or letra == "O":
        numero_vogais += 1
    if letra == "u" or letra == "U":
        numero_vogais += 1

print(f"Numero de vogais = {numero_vogais}")

"""
if letra in "aeiouAEIOU":
        numero_vogais += 1
"""
