import random


def jogar():
        print("*************************")
        print("***Jogo de adivinhação***")
        print("*************************")

        numero_do_game = random.randrange(0,101)

        pontos = 100
        total_tentativas = 0

        print("Defina uma dificuldade")
        dificuldade = int(input("Digite (1) para fácil, (2) para médio ou (3) para difícil:"))

        print(dificuldade)

        if(dificuldade == 1):
            chances = 20
        elif(dificuldade == 2):
            chances = 10
        elif(dificuldade == 3):
            chances = 5



        pontos_rodada = int(pontos/chances)

        for rodada in range(1,chances + 1):

            print("Rodada número {} de {} chances!".format(rodada , chances))

            numero_chutado = int(input("Digite um número de 0 a 100:"))

            if(numero_chutado == numero_do_game):
                print("Você venceu!Parabéns fez {} pontos".format(pontos))
                break
            elif(numero_chutado < numero_do_game):
                pontos = pontos - pontos_rodada
                print("Você errou, o número é maior que o chute!")
            elif(numero_chutado > numero_do_game):
                pontos = pontos - pontos_rodada
                print("Você errou, o número é menor que o chute!")


if (__name__ == "__main__"):
    jogar()