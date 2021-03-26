# 10. Faça um programa que receba dois números inteiros
# e gere os números inteiros que estão no intervalo
# compreendido por eles.

print('Números no intervalo dos digitados')
n1 = int(input('Digite um número:  '))
n2 = int(input('Digite outro:  '))

if n1 < n2:
    for i in range(n1 + 1, n2, 1):
        print(i, end=', ')

else:
    a = n2
    b = n1
    for i in range(a + 1, b, 1):
        print(i, end=', ')
