"""
Escreva o cabeçario do módulo.

"""


def entrada() -> list:
    """
    Escrever a docstring da função
    """
    num_1 = float(input("\nDigite o primeiro número: "))
    num_2 = float(input("\nDigite o segundo número: ")) 
    return [num_1, num_2]


def saida(valor: float):
    """
    Escreva o docstring
    """
    print(f"\nO resultado da operação é igual a {valor}.")