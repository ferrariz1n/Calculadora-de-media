def Resultado(n1,n2,n3):

#calcula a media e printa os mesmos

        media=(n1+n2+n3)/3
        print("Nota 1: ",n1)
        print("Nota 2: ",n2)
        print("Nota 3: ",n3)
        print("Media: %.1f"% media)

#define se aprovado ou reprovado de acordo com a nota

        if media>=7:
            print("Aprovado")
        else:
            print("Reprovado")

 #retorna os valores para serem puxados para o salvarnotas

        return n1,n2,n3,media