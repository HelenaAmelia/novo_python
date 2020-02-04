from datetime import date

ano = int(input('Digite o ano de nascimento do atleta:'))

cores = {'azul': '\033[1;33m',
         'limpa': '\033[m',
         'bold': '\033[1m'}

idade = date.today().year - ano

print('O atleta de {}{}{} anos está na categoria:'.format(cores['bold'],  idade, cores['limpa']))

if idade <= 9:
    categoria = 'MIRIM'
    rang = '(até 9 anos)'

elif idade <= 14:
    categoria = 'INFANTIL'
    rang = '(até 14 anos)'

elif idade <=19:
    categoria = 'JUNIOR'

elif idade <=25:
    categoria = 'SÊNIOR'

else:
    categoria = 'MASTER'

print('{}{}!'.format(cores['azul'], categoria))
