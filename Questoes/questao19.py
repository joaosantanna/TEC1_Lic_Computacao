print("Lista de divisores de um numero")

n = int(input("Informe o numero:"))
print("lista de divisores")
contador = 0
for i in range(n, 0, -1):
    if n % i == 0:
        print(i)
        contador += 1

print(f"O numero de divisores = {contador}")
