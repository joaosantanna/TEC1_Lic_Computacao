soma = 0
for i in range(100, 201):
    if i % 7 == 0:
        print(i)
        soma += i

print(f"A soma dos numeros divisiveis = {soma}")
