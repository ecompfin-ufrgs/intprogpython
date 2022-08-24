"""
Programa soma
Requisitos: Este programa lê dois números digitados pelo usuário
calcula a soma deles e coloca o resultado na tela.
Autor: Nelson S. dos Santos
Data: 23/08/2022
Versão: 1.0.0
"""
# Importação de módulos

import entrada
import processa
import saida



# Definição de funções



def main():
    # Entrada
    lista = entrada.entra_dados()

    # Processamento
    soma = processa.adicao(lista[0], lista[1])

    # Saída
    saida.impressora(soma, lista[0], lista[1]) 
    


 
# Execução do programa

if __name__ == "__main__":
    main()








