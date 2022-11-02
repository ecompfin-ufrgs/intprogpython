"""
Programa: soma
Requisito (problema que o programa resolve):
Ler um conjunto de números reais digitados pelo usuário, calcular
a soma deles e colocar o resultado na tela.
Autor: Nelson S. dos Santos
Data: 31-10-2022
Versão: 0.0.5
"""

# Entrada e Processamento de dados


soma = 0

while True:
    numero = input("\nDigite a parcela ou pressione a tecla X para interromper: ")
    if numero == "X":
        break
    soma = soma + float(numero) 
    


# Saida  de dados

print(f"\nA soma dos números digitados é igual a {soma}.")
