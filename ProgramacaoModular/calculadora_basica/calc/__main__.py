"""Programa calculadora_basica
Requisitos: Faça um programa de terminal que leia dois números
digitados pelo usuário e a operação desejada entre (adição,
subtração, multiplicação e divisão) e coloque o resultado na
tela.

Autor: Eu
Data: Hoje
Versão: 0.0.1

"""

# Importação de módulos

import model
import view


def main():
    # entrada
    dados = view.entrada()

    # processamento
    if dados[2] == "+":
        resultado = model.adicao(dados[0], dados[1])
    elif dados[2] == "-":
        resultado = model.subtracao(dados[0], dados[1])
    elif dados[2] == "*":
        resultado = model.multiplicacao(dados[0], dados[1])
    elif dados[2] == "/":
        resultado = model.divisao(dados[0], dados[1])
    else:
        print("A operação não está definida.")

    # saida
    view.saida(dados[0], dados[1], dados[2], resultado)

if __name__ == "__main__":
    main()
        
