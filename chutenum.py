import random


random_nume = random.randint(1, 10)


while True:
    num = int(input("Chute um número de 1 até 10: "))
    if num > random_nume:
        j = str(input("Sua resposta foi a cima do número certo, Você deseja continuar?(s/n):"))
        if j == 's':
            pass
        else:
            print("O número aleatório que você não acertou é {}".format(random_nume))
            break

    elif num < random_nume:
        i = str(input("Sua resposta foi a baixo do número certo, você deseja continuar?(s/n):"))
        if i == 's':
            pass
        else:
            print("O número aleatório que você não acertou é {}".format(random_nume))
            break    
    
    elif num == random_nume:
        print("Parabéns você acerto o número:{}".format(random_nume))
        break