# 23. Faça um programa que mostre todos os primos entre 1 e N
# sendo N um número inteiro fornecido pelo usuário. O programa
# deverá mostrar também o número de divisões que ele executou
# para encontrar os números primos. Serão avaliados o funcionamento,
# o estilo e o número de testes (divisões) executados.


n = int(input('Digite um número:  '))

cont = 0
lista = []

for i in range(0, n):
    if n % (i + 1) == 0:
        cont += 1
        lista.append(i + 1)
    else:
        cont
if cont == 2:
    print(f'O número {n} é primo')
    print(f'O número {n} foi dividido {cont} vezes\
 para achar seus primos {lista}')
else:
    print(f'O número {n} não é primo')
    print(f'O número {n} é divisível por {lista}')
    print(f'O número {n} foi dividido {cont} vezes')
