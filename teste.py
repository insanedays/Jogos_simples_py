import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras = ["_" for letra in palavra_secreta]

    enforcou = False
    venceu = False
    erros = 0

    print(letras)
    print(palavra_secreta)

    while(not enforcou and not venceu):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras[index] = letras
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        venceu = "_" not in letras
        print(letras)

    if(venceu):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
