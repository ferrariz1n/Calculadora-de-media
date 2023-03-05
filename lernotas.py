def Lernotas():
#entrada de dados
    n=float(input("Digite uma nota para o aluno(a): "))
# recebe valores de 0 a 10
    if n>=0 and n<=10:
        return n
# finaliza o programa
    if n==-999:
        exit()

#define como valor invalido
    else:
        print("Valor invalido")
        return Lernotas()