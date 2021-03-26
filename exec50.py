# 50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
# Faça um programa que calcule o valor de H com N termos.



h = 1
n = 2
lista_h = []
lista_n = []
print('H = 1 + ', end='')
while n <= 10 - 1:
    print(f' {h} / {n} + ', end='')
    lista_h.append(h)
    lista_n.append(n)
    n += 1

print(f'{h} / {n} => {sum(lista_h)} / {sum(lista_n)} =>\
{sum(lista_h)} / {sum(lista_n)}')
