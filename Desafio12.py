print('Desafio 12 - Olha a Promoção')
print('Na compra de qualquer produto, receba 5% de desconto')
n1 = float(input('Sua blusa custa R$ '))
print('Você ganhou 5% de desconto na nossa promoção')
desc = n1 - (n1 * (5/100))
print('Com o desconto sua blusa sai por R$ {:.2f}'.format(desc))
