# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada
# de qualquer número inteiro entre 1 a 10. O usuário deve informar
# de qual numero ele deseja ver a tabuada. A saída deve ser conforme
# o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 10 = 50

'''num = int(input('Digite um número para ver a tabuada: '))

for n in range(10):
    print('{} x {} = {}'.format(num, n + 1, num * (n + 1)))'''


numero = int(input('Que tabuada gostaria de ver? de 1 a 10:  '))

print(f'Tabuada do número: {numero}')
for i in range(1, 11):
    print(f'{numero} X {i} = {numero * i}')
