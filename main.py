#importa as bibliotecas
from lernotas import Lernotas
from resultado import Resultado
from salvarnotas import Salvarnotas

def Main():
    a = Lernotas()
    b = Lernotas()
    c = Lernotas()



    n1,n2,n3,media = Resultado(a,b,c)
    

    
    Salvarnotas(n1,n2,n3,media)

    return Main()
        
Main()


#criar um executavel
#executavel em python 
#pip install pyinstaller
#pyinstaller --onefile seu_script.py

