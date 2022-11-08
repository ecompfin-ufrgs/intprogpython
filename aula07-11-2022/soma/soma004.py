"""
Programa soma
Requisito: Este programa pega dois números digitados pelo
usuário, calcula a sua soma e coloca o resultado na tela,
com uma frase que explique o que é o resultado obtido.
Autor: Nelson S. dos Santos
Data: 07/11/2022
Versão: 0.0.4
"""

def soma(x, y):
    return x + y


# Entrada

numero_1 = float(input("Digite a primeira parcela: "))

numero_2 = float(input("Digite a segunda parcela: "))



# Processamento

valor = soma(numero_1, numero_2)

# Saída

print(f"A soma dos números {numero_1} e {numero_2} é igual a {valor} .")




