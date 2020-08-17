
def jogar():
    print("*************************")
    print("******Jogo de forca******")
    print("*************************")

    enforcou = False
    acertou = False
    palavra_secreta = "banana".upper()
    letras = ["_" for palavras in palavra_secreta]
    print(letras)

#enquanto não acertou e nao enforcou#
    while not enforcou and not acertou :
        chute = input("Insira a letra:")
        chute = chute.upper()

        if(chute in palavra_secreta):
            posicao_palavra = 0

            for palavra in palavra_secreta:
                if (chute == palavra):
                    letras[posicao_palavra] = palavra
                    print(letras)


                posicao_palavra +=1  #Como o for percorre a palavra na ordem, ela encontra a posição da letra, pq a var acompanha o numero referente as vezes loop!#




if (__name__ == "__main__"):
    jogar()




