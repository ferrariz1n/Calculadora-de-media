import resultado

#abre o bloco de notas

def Salvarnotas(n1,n2,n3,media):
    with open("bdnotas.txt", "a") as bdnotas:

#f formata a string
#wirite escreve em notas

        bdnotas.write(
            f"\nNota1: {n1}"
            f"\nNota2: {n2}"
            f"\nNota3: {n3}"
            f"\n---------------"
            f"\nMedia: {media}\n"
            )
