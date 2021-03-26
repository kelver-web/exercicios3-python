# 11. Altere o programa anterior para mostrar no final a soma dos números.


print('Números no intervalo dos digitados mais sua soma')
n1 = int(input('Digite um número:  '))
n2 = int(input('Digite outro:  '))

lista = []

if n1 < n2:
    for i in range(n1 + 1, n2):
        lista.append(i)

elif n2 < n1:
    for i in range(n2 + 1, n1):
        lista.append(i)
print(f'A soma dos números da lista é = {sum(lista)}')
