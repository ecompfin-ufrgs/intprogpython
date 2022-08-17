"""
Programa tamanho_lista
Requisitos: Este programa calcula o tamanho de uma lista Python dada pelo usuário
e o coloca na tela.
Autor: Eu
Data: Hoje
Versão: 0.0.1
"""

# Entrada
# entrada do usuário pelo teclado

lista = []
while True:
    elemento = input("\nDigite um elemento para a sua lista. Quando encerrar, digite X e pressione ENTER.  ")
    if elemento.upper() == "X":
        break
    lista.append(elemento)


# Processamento
# calcula o tamanho de uma lista Python
tamanho_lista = len(lista)

# Saída 
# colocar o tamanho da lista na tela.

print(f"A lista lista digitada foi {lista} e seu tamanho é {tamanho_lista}.")
