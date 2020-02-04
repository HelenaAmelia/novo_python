valor = float(input('Entre com o valor do produto R$:'))
modo = int(input('Escolha o modo de pagamento!\n Digite 1 para pagamento a vista. \n Digite 2 para pagamento no cartao.'))

while valor < 0 or modo < 0:
    print('Valor ou modo de pagamento inválidos!')
    valor = float(input('Entre com o valor do produto R$:'))
    modo = int(input('Escolha o modo de pagamento!\n Digite 1 para pagamento a vista. \n Digite 2 para pagamento no cartao.'))


if modo == 2:
    modo = int(input('Digite o numero de parcelas ou 0 para pagamento a vista:'))

if modo == 1:
    desc = '10% de desconto'
    valor = 0.9*valor

elif modo == 0:
    desc = '05% de desconto'
    valor = 0.95 * valor

elif modo < 3:
    desc = 'nenhum desconto'

else:
    desc = '20% de juros'
    valor = 1.20 * valor


print('Você teve {} sobre o valor do produto! O preço final a ser pago é R${}.'.format(desc, valor))