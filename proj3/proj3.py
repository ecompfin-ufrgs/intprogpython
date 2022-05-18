
import requests
import webbrowser

pagina = requests.get('https://g1.globo.com/politica/')
print(pagina.status_code)

with open('politica.html', 'wb') as arquivo:
    for texto in pagina.iter_content(1048576):
        arquivo.write(texto)

"""
arquivo = open('politica.html', 'wb')
for texto in pagina.iter_content(1048576):
    arquivo.write(texto)
arquivo.close
"""


webbrowser.open('politica.html')

