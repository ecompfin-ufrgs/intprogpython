"""
Programa dobro
Requisitos: Este programa lê um número digitado pelo usuário e
imprime na tela o seu dobro.
Autor: Eu
Data: Hoje
Versão: 0.0.1
"""

## Definição de funções

# Entrada

def entrada():
    """Leitura do teclado do usuário."""
    numero = float(input("\nDigite um número: "))
    return numero



# Processamento

def dobro(x):
    return 2*x



# Saida

def saida(x, y):
    print(f"\nO dobro do número {x} é igual a {y}.")

# Função principal

def main():
    # Entrada de dados
    valor = entrada()
    
    # Cálculo do dobro do valor digitado pelo usuário
    dobro_valor = dobro(valor)
    

    # Saída de dados
    saida(valor, dobro_valor)

## Execução da função principal
if __name__ == "__main__":
    main()

