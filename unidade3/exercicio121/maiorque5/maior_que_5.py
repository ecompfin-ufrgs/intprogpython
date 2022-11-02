"""
Programa maior que 5
Requisito: Leia um número digitado pelo usuário e diga se ele é
maior do que 5.
Autor: Eu
Data: hoje
Versão: 0.0.1
"""



# Entrada

numero = float(input("\nDigite um número real: "))

# Processamento

if numero > 5:
    frase = f"O número {numero} é maior que 5."
elif numero == 5:
    frase = f"O número {numero} é igual que 5."
else:
    frase = f"O número {numero} é menor que 5."

# Saida

print(frase)
