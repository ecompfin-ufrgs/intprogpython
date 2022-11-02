"""
Programa: exercicio1-3-3
Requisitos:
Leia cinco números e imprima na tela o quadrado de cada um deles.

Autor: Eu
Data: Hoje
Versão: 0.0.1
"""


# Entrada, processamento e saída

i = 0

while i < 5:
    numero = float(input("\nDigite um número: ")) # entrada
    print(f"\nO quadrado do número digitado é igual a {numero**2}") # processamento e saida
    i += 1 # i = i + 1
