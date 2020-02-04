reta1 = float(input('Digite o comprimento da primeira reta:'))
reta2 = float(input('Digite o comprimento da segunda reta:'))
reta3 = float(input('Digite o comprimento da terceira reta:'))


cores = {'azul': '\033[1;33m',
         'limpa': '\033[m',
         'bold': '\033[1m'}


if (reta1 < reta2 + reta3 and reta1 > abs(reta2 - reta3)) and (
        reta2 < reta1 + reta3 and reta2 > abs(reta1 - reta3)) and (
        reta3 < reta2 + reta1 and reta3 > abs(reta2 - reta1)):

    if reta1 == reta2 == reta3:
        triang = 'EQUILÁTERO'

    elif reta1 != reta2 != reta3 != reta1:
        triang = 'ESCALENO'

    else:
        triang = 'ISÓSCELES'

    print('As retas de comprimento {}{}, {} e {}{} formam um triângulo {}{}!'.format(cores['bold'], reta1, reta2, reta3, cores['limpa'], cores['azul'], triang))

else:
    print('As retas {}NÃO{} formam um triângulo!'.format(cores['bold'], cores['limpa']))
