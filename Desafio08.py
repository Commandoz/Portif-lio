print('Desafio 08 - Metros para Centímetros e Milimetros')
print('Digite a quantidade em Metros para transformar em Centímetros e Milimetros')
m = float(input('Quantidade em Metros: '))
cent = m * 100
mil = m * 1000
print('Sua conversão resultou em {:.0f} centímetros ou {:.0f} mílimetros'.format(cent, mil))