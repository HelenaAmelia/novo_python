alt = float(input('Digite sua altura em metros:'))
peso = float(input('Digite seu peso em kg:'))

imc = peso/pow(alt, 2)

if imc < 18.5:
    cond = 'abaixo do peso'

elif imc <=25:
    cond = ' peso ideal'

elif imc <= 30:
    cond = 'sobrepeso'

elif imc <= 40:
    cond = 'obesidade'

else:
    cond = 'obesidade mórbida'

print('Seu imc é de:{}. Seu status é {}!'.format(imc, cond))