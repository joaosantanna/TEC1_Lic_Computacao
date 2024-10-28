print("Informe as dimensoe da piscina ...em metros")
comprimento = float(input("Informe o comprimento:"))
profundidade = float(input("Informe a profundidade:"))
largura = float(input("Informe a largura :"))

volume = comprimento * profundidade * largura
print(f"O volume de agua da piscina = {volume} metros cubicos")

tempo = volume / 20

print(f"O tempo necessario para encher a piscina = {tempo:.2f} minutos")
