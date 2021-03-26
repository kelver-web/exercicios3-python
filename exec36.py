# 36. Desenvolva um programa que faça a tabuada de um número
# qualquer inteiro que será digitado pelo usuário, mas a tabuada
# não deve necessariamente iniciar em 1 e terminar em 10,
# o valor inicial e final devem ser informados também pelo
# usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

from time import sleep
from colorama import Fore, init
init(convert=True)

while True:
    num = int(input('Digite um número para ver sua tabuada:  '))
    print(f'MONTAR A TABUÁDA DE {num}')
    n_inicial = int(input('Começar por:  '))
    n_final = int(input('Terminar por:  '))
    if n_final < n_inicial:
        print('O número final precisa ser maior que o númro inicial')
    else:
        print(f'Vou montar a tabuada de {num} começando por {n_inicial}\
 e terminando em {n_final}')
        sleep(2)

    for i in range(n_inicial, n_final + 1):
        sleep(1)
        print(Fore.GREEN + f'{num} x {i} = {num * i}', Fore.WHITE)

    continua = input('Deseja continuar?  [S] ou [N]:  ')

    if continua in 'Ss':
        continue
    elif continua in 'Nn':
        print('Programa finalizado.')
        break
