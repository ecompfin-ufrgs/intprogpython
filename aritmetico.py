"""Modulo aritmetico
Descrição: 
Este módulo fornece funções aritméticas básicas.
Autor; Nelson
Data: 26/04/2022
Versão: 1.0.0"""


def adicao(x: float, y: float) -> float:
    """
    Docstring de documentação da função.  Esta função soma dois números.
    """
    return x + y


def subtracao(x: float, y: float) -> float:
   """
   Esta função subtrai um número y de um número x.
   """
   return x - y

def multiplicacao(x: float, y: float) -> float:
    """
    Esta função multiplica dois números.
    """
    return x*y


def divisao(x: float, y: float) -> float:
    """
    Esta função pega dois números tais que o segundo é diferente de zero
    e calcula a sua divisão.
    """
    if y == 0:
        return "Não se pode dividir por zero."
    return x/y

