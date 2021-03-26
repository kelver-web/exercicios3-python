# 28. Faça um programa que calcule o valor total investido
# por um colecionador em sua coleção de CDs e o valor médio
# gasto em cada um deles. O usuário deverá informar a quantidade
# de CDs e o valor para em cada um.

from colorama import Fore, init
init(convert=True)


cds = int(input("Informe a quantidade de CD's que você comprou?  "))

lista = []

for i in range(cds):
    valor = float(input(f'Informe o valor do {i + 1}º CD:  '))
    lista.append(valor)

    soma = sum(lista)
    media = soma / len(lista)

print(f'Total gasto na coleção R$ {Fore.YELLOW + str(soma)}0', Fore.WHITE)
print(f'Média de gasto em cada CD foi de {Fore.BLUE + str(media)}0')
