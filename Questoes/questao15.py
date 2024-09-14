# entradas
peso = float(input("Digite seu peso(KG):"))
altura = float(input("Digite sua altura(m):"))

# processamento + saida
imc = peso / altura**2

print(f"IMC = {imc:.2f}")  # formata o valor de imc para
# duas casas decimais depois do ponto

if imc < 20:
    print("Abaixo do peso ideal")
elif 20 <= imc <= 25:
    print("Peso ideal")
else:
    print("Acima do peso ideal")
