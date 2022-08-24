"""
Função entra_dados
Requisitos: Esta função lê dois números digitados pelo usuário.
Autor: Nelson S. dos Santos
Data: 23/08/2022
Versão:0.9.0
"""
# Definição de funções


def entra_dados():
    """Esta função (procedimento) lê dois números digitados pelo usuário."""
    i = 0
    lista_numeros = []
    while i < 2:
        numero = float(input("\nDigite um número: "))
        lista_numeros.append(numero)
        i+=1
    return lista_numeros
