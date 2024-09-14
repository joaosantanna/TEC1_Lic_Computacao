x = int(input("Digite um numero inteiro:"))

if x % 2 == 0:  # operador mod(%) retorna o resto da divisao inteira
    # de x por 2 ... qualquer numero par dividio por 2 o resto = 0
    print(f"numero {x} é par")
else:
    print(f"numero {x} é impar")
