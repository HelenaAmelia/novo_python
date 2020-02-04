from random import randint
from time import sleep

jogar = input('Digite qualquer tecla para jogar ou N para sair: ')

vitoria = 0
derrota = 0

while jogar != 'N':
    itens = ['Pedra', 'Papel', 'Tesoura']

    mao_pc = randint(0, 2)

    mao = int(input('Sua vez!\n Escolha 0 para pedra, 1 para papel ou 2 para tesoura:'))

    while mao not in range(0,3):
        mao = int(input('Jogada inválida.Escolha 0 para pedra, 1 para papel ou 2 para tesoura:'))

    print('JO', end='')
    sleep(1)
    print('KEN')
    sleep(1)
    print('POOO')
    sleep(1)

    if mao_pc == 0:
        if mao == 0:
            print('EMPATE')

        elif mao == 1:
            print('VOCÊ GANHOU!!')
            vitoria += 1

        else:
            print('VOCÊ PERDEU!')
            derrota += 1

    elif mao_pc == 1:
        if mao == 0:
            print('VOCÊ PERDEU!')
            derrota += 1

        elif mao == 1:
            print('EMPATE')

        else:
            print('VOCÊ GANHOU!!')
            vitoria += 1
    else:
        if mao == 0:
            print('VOCÊ GANHOU!')
            vitoria += 1

        elif mao == 1:
            print('VOCE PERDEU')
            derrota += 1

        else:
            print('EMPATE!!')

    print('Computador:{} \n jogador:{}'.format(itens[mao_pc], itens[mao]))
    jogar = input('Digite qualquer letra para jogar ou N para sair: ').upper().strip()[0]

print('O jogo acabou! \n Numero de vitórias:{} \n Numero de derrotas:{}'.format(vitoria, derrota))
