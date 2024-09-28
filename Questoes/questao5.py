lado = float(input("informe o valor do lado do quadrado:"))
area_quadrado = lado**2

base = float(input("Informe a base do triangulo:"))
altura = float(input("Informe a altura do triangulo:"))
area_tri = base * altura / 2

base_maior = float(input("Informe o valor da base maior do trapezio:"))
base_menor = float(input("Informe o valor da base menor do trapezio:"))
altura_trapezio = float(input("Informe o valor da altura do trapezio:"))
area_trapezio = (base_maior + base_menor) * altura / 2

print(f"area do quadrado = {area_quadrado}")
print(f"area do triangulo = {area_tri}")
print(f"area do trapezio = {area_trapezio}")

if area_quadrado > area_tri and area_quadrado > area_trapezio:
    print("area do quadrado é a maior")
elif area_tri > area_quadrado and area_tri > area_trapezio:
    print("area do triangulo é a maior")
else:
    print("area do trapezio é a maior")
