
# Importando o pacote requests

import requests

def page_reader(endereco: str) ->  requests.models.Response:
    pagina = requests.get(endereco)
    return pagina

def grava_pagina_web(resposta: requests.models.Response) -> None:
    arquivo = open('politica.html', 'wb')
    for texto in resposta.iter_content():
        arquivo.write(texto)
    arquivo.close()

    
def main():
    endereco = 'https://g1.globo.com/politica/'
    politica = page_reader(endereco)
    grava_pagina_web(politica)
    print(f"A página {endereco} foi gravada com sucesso no arquivo 'politica.html'.")
    
if __name__ == "__main__":
    main()