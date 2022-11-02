"""
Programa: exercicio1-2-1
Requisitos:
Leia um número e imprima na tela o seu dobro se ele for menor do
que 10. Se o número for de 10 até 20, imprima a sua metade.
Em qualquer outro caso, imprima na tela que o número n˜ao é válido.
Autor: Eu
Data: Hoje
Versão: 0.0.1
"""


# Entrada


numero = float(input("Digite um número: "))

# Processamento



if numero < 10:
    resultado = f"\nO resultado é igual a {2*numero}."

elif (numero >= 10) and (numero <=20):
    resultado = f"O resultado é igual a {numero/2}"

else:
    resultado = "O número não é válido."

               


# Saída

print(resultado)



