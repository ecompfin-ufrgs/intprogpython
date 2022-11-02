"""
Programa: soma
Requisito (problema que o programa resolve):
Ler 4 números reais digitados pelo usuário, calcula a sua soma e
colocar o resultado na tela.
Autor: Nelson S. dos Santos
Data: 31-10-2022
Versão: 0.0.4
"""

# Entrada e Processamento de dados

i = 0 # contador
soma = 0

# Laço (loop) de repetição
while i < 4:
    #print(i)
    numero = float(input("\nDigite a parcela: "))
    soma = soma + numero # acumulador
    i = i + 1


# Saida  de dados

print(f"\nA soma dos números digitados é igual a {soma}.")
