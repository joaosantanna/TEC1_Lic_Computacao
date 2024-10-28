print("Testar se o numero é primo")
n = int(input("Informe o numero:"))
eh_primo = True
for i in range(n - 1, 1, -1):
    if n % i == 0:
        eh_primo = False
        break

if eh_primo:
    print(f"O numero {n} é primo")
else:
    print(f"O numero {n} não é primo")
