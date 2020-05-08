print('Desafio 11 - Vamos pintar a parede?')
print('Vamos ver quantos litros de tinta precisamos para sua parede')
alt = float(input('Qual a altura da parede? '))
comp = float(input('Qual o comprimento da parede? '))
tam = alt * comp
print('Sua parede tem {:.2f} metros quadrados'.format(tam))
tint = tam / 2
print('Para pintar sua parede são necessários {:.2f} litros de tinta'.format(tint))
