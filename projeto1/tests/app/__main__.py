

def main():
    import utilitarios
    
    diretorios = []
    while True:
        diretorio = input("\nDigite o nome do diretório que deseja criar.  Se quiser parar, digite pare. ")
        diretorio = diretorio.upper()
        if diretorio == "PARE":
            break
        else:
            diretorios.append(diretorio.lower())
    for dir in diretorios:
        utilitarios.cria_diretorio(dir)
    
    move_planilha_documento()

if __name__ == "__main__":
    main()
    
