# 32. Faça um programa que calcule o fatorial de um número
# inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

numero = int(input('digite um número para caucular seu fatorial:  '))
cont = numero
fat = 1

print(f'Cauculando o fatorial de {numero}!', end=' = ')

while cont > 0:
    print(f'{cont}', end='')
    print(' . ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f'{fat}')
