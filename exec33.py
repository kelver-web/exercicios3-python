# 33. O Departamento Estadual de Meteorologia lhe contratou
# para desenvolver um programa que leia um conjunto
# indeterminado de temperaturas, e informe ao final a menor
# e a maior temperaturas informadas, bem como a média das temperaturas.

from colorama import Fore, init
init(convert=True)

print('|###############################################################|')
print(Fore.YELLOW + '|      ==== Departamento Estadual de Meteorologia ====          |', Fore.WHITE)
print('|###############################################################|')
n_temp = int(input('Digite a quantidade de temperaturas:  '))


lista = []

for i in range(n_temp):
    temp = float(input(f'digite a {i + 1}º temperatura:  '))
    lista.append(temp)
print(Fore.BLUE+'|===============================================================|')
print('|A menor temperatura foi --> {}°C                             |'.format(min(lista)))
print('|A maior temperatura foi --> {}°C                             |'.format(max(lista)))
print('|A média das temperaturas foi de --> {:.2f}C°                    |'.format(sum(lista) / len(lista)))
print('|===============================================================|')