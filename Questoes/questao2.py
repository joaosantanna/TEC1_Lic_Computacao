'''
Programa que le uma temperatura em farenheit
e converte para celcius
entrada : valor da temperatura em Farenheit ( float)
saidas: valor da temperatura em celcius
autor: joao santanna
data: 06/09/2024
'''
F = float(input('Digite a temperatura em Farenheit:'))

C = (F - 32)/1.8

print(f'A tempertura de {F} Farenheit = {C:.2f} Celcius')
