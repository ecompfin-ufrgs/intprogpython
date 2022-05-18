def cria_diretorio(nome_diretorio: str):
    """
    Esta função cria diretórios se eles não existirem.
    """
    import os
    if os.path.exists(nome_diretorio) == False:
        os.mkdir(nome_diretorio)

        
def move_planilha_documento():
    """
    Esta função move o arquivo para o diretório desejado.
    """
    import os
    import shutil
    
    arquivos = os.listdir()
    
    for arquivo in arquivos:
        if ".xls" in arquivo:
            shutil.move(arquivo, f"./planilha/{arquivo}")
            elif ".doc" in arquivo:
                shutil.move(arquivo, f"./documentos/{arquivo}")
                
                
                
                