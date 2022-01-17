import random 
    
jokenpo = ['pedra', 'papel', 'tesoura']
computador = (random.randint(0, 2))
player = int(input('''Escolha entre:
[0] pedra
[1] papel
[2] tesoura 
: '''))

print('=' *50)
print("O computador escolheu {}".format(jokenpo[computador]))
print("Você escolheu {}".format(jokenpo[player]))
print('=' * 50)

if computador == 0:
    if player == 0:
        print("Empate")
    elif player == 1:
        print("Parabéns você ganhou!!")
    else:
        print("Infelizmente você perdeu.")

if computador == 1:
    if player == 1:
        print("Empate!")
    elif player == 2:
        print("Parabéns, você ganhou!!")
    else:
        print("Infelizmente você perdeu.")

if computador == 2:
    if player == 2:
        print("Empate")
    elif player == 1:
        print("Parabéns você ganhou!!")
    else:
        print("Infelizmente você perdeu.")