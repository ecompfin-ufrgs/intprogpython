"""
Façam o cabeçario.
"""

# Importação de módulo

import aritmetico
import es

# Definição de funções

def main():
    lista_numeros = es.entrada()
    operacao = input("""Qual operação você deseja?  Digite:
             + para adição,
             - para subtração,
             x - para multiplicação ou
             / para divisão\n""")
    
    if operacao == "+":
        valor = aritmetico.adicao(lista_numeros[0], lista_numeros[1])
    elif operacao == "-":
        valor = aritmetico.subtracao(lista_numeros[0], lista_numeros[1])
    elif operacao == "x":
        valor = aritmetico.multiplicacao(lista_numeros[0], lista_numeros[1])
    elif operacao == "/":
        valor = aritmetico.divisao(lista_numeros[0], lista_numeros[1])
    else:
        valor = "Esta operação não está definida para esta calculadora."
    es.saida(valor)

if __name__ == "__main__":
    main()