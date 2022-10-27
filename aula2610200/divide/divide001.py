"""Programa divide
Requisito: Crie um programa que leia dois números inteiros
do teclado, calcule a razão entre o primeiro e o segundo e
escreva na tela o resultado.
Autor: Nelson S. dos Santos
Versão: 0.0.1
"""




# Entrada

print("Este programa calcula a razão entre dois números dados pelo usuário")

numerador = float(input("\nDigite o numerador: "))

denominador = float(input("\nDigite o denominador: "))



# Processamento

razao = numerador / denominador

# Saída

print(f"A razão entre o número {numerador} e o número {denominador} é igual a {razao} .")
