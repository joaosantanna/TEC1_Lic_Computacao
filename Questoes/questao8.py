# entradas
gasto = float(input('Informe o valor da conta:R$'))
percentual_gorjeta = float(input('Informe o percentual de gorjeta:') )

# processamentos
valor_gorjeta = gasto * percentual_gorjeta/100
total = gasto + valor_gorjeta

# saida
print(f'O valor da gorjeta = R${valor_gorjeta:.2f}')
print(f'Valor total da conta = R${total:.2f}')


