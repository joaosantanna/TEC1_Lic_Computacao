"""
Programa para sortear uma questão da lista
de exercicios
Keyword arguments: nenhum
Return: um numero int da questao sorteada
"""

from random import randint

INICIO = 1
FIM = 16

questao = randint(INICIO, FIM)

print(f"Questao sorteada = {questao}")
