"""
Programa acessa_lista
Requisitos: Acessar elementos de uma lista com os números 1,4,7.
Autor: Eu
Data: hoje
Versão: 0.0.4 - introduz a estrutura de controle de fluxo for com range
"""

# Entrada de dados

lista = [1, 4, 7]


# Processamento de dados



# Saída de dados
"""
while i < 3:
    print(f"O elemento {i + 1} da lista é {lista[i]}")
    i+=1
"""

for i in list(range(3)):
    print(f"\nO elemento {i} da lista é {lista[i]}.")
