"""Módulo view.py
Requisito: Este módulo agrega as funções de entrada e saída de dados
Autor: Eu
Data: Hoje
Versão: 0.0.1
"""

def entrada():
    """Esta função lê o teclado da calculadora."""
    i = 0
    dados = []
    while i < 2:
        dados.append(float(input(f"\n Digite o número {i+1}: ")))
        i += 1
    operacao = input("""\nDigite a operação desejada:
                     (+) para adição;
                     (-) para subtração;
                     (*) para multiplicação, e
                     (/) para divisão: """)
    dados.append(operacao)
    return dados




def saida(numero_1, numero_2, op, result):
    """Esta função escreve na tela do usuário o resultado
    da operação realizada na calculadora."""
    print(f"""O resultado da operação de {op} sobre
os números {numero_1} e {numero_2} é igual a {result}.""")