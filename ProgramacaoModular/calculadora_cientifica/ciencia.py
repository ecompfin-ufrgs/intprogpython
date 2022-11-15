"""
Módulo ciencia.py
Requisitos:
Este módulo provê as seguintes funções de calculadora científica:

1. Exponenciação
2. Radiciação
3. Seno
4. Cosseno
Autor: Eu
Data: Hoje
Versão: 0.0.1
"""

# Importação de módulos

import math 

def exponenciacao(base, expoente):
    "Esta função calcula a operação de exponenciação"""
    return base**expoente

def radiciacao(radicando, indice):
    "Esta função calcula a operação de radiciação"""
    return math.pow(radicando, 1/indice)

def seno(angulo_radianos):
    "Esta função calcula a operação de exponenciação"""
    return math.sin(angulo_radianos)

def cosseno(angulo_radianos):
    "Esta função calcula a operação de exponenciação"""
    return math.cos(angulo_radianos)

