# 42. Faça um programa que leia uma quantidade indeterminada de
# números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de
# dados deverá terminar quando for lido um número negativo.


lista25 = []
lista50 = []
lista75 = []
lista100 = []

numero = True
print('DIGITE UM NÚMERO NEGATIVO PARA SAIR')
while numero > 0:
    numero = int(input('Digite um número: '))
    if numero > 0 and numero <= 25:
        lista25.append(numero)
    elif numero > 25 and numero <= 50:
        lista50.append(numero)
    elif numero > 50 and numero <= 75:
        lista75.append(numero)
    elif numero > 75 and numero <= 100:
        lista100.append(numero)
print()
print('INTERVALOS DE [0, 25]')
print(f'{lista25}')
print()
print('INTERVALOS DE [26, 50]')
print(f'{lista50}')
print()
print('INTERVALOS DE [51, 75]')
print(f'{lista75}')
print()
print('INTERVALOS DE [76, 100]')
print(f'{lista100}')
