x = float(input("Digite um valor para x:"))
y = float(input("Digite um valor para y:"))

# troca os valores de x por y em um unico comando
x, y = y, x

# em outra linguagens esse comando não existe
# nessa caso vc tem que fazer a troca em 3 etapas salvando
# o valor de uma das variaveis para uma terceira variavel temporaria
"""
temp = x # valor original de x gravado em temp
x = y
y = temp # y recebe o valor original de x 
"""

print(f"X ={x}")
print(f"Y = {y}")
