# 22. Altere o programa de cálculo dos números primos,
# informando, caso o número não seja primo, por quais
# número ele é divisível.

num = int(input('Digite um numero: '))
cont = 0
lista = []

for i in range(num):
    if num % (i + 1) == 0:
        cont += 1
        lista.append(i + 1)
    else:
        cont
if cont == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
    print(f'O número {num} é divisível por {lista}')
