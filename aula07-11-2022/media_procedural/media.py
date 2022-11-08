# Definição de funções

def entrada():
    """Entrada de dados"""
    soma = 0
    i = 0
    x = [ 1 , 7 , 15 , 31]
    return [soma, i, x]

def calcula_media(soma, i, x):
    """Processamento de dados"""
    while i < len(x):
        soma = soma + x[i]
        i+=1
        media = soma/len(x)
    return media

def saida(x):
    """Saída de dados"""
    print(f'A média dos números é igual a {x}.')

def main():
    valores = entrada()
    media = calcula_media(valores[0], valores[1], valores[2])
    saida(media)

# Execução da função principal

main()



