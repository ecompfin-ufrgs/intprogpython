"""
Programa multiplica
Requisito: Este programa pega dois números digitados pelo
usuário, calcula o produto dele e coloca o resultado na tela,
com uma frase que explique o que é o resultado obtido.
Autor: Nelson S. dos Santos
Data: 26/10/2022
Versão: 0.1.2
Correção do bug: chamar de parcela o que é, na verdade, fator.
Inclusão de funcionalidade: informar o usuário para que serve o
programa.
"""

# Entrada
print("Este programa calcula o produto de dois números dados pelo usuário")

numero_1 = float(input("\nDigite o primeiro fator: "))

numero_2 = float(input("\nDigite o segundo fator: "))



# Processamento

produto = numero_1 * numero_2

# Saída

print(f"O produto dos números {numero_1} e {numero_2} é igual a {produto} .")




