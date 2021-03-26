# 18. Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.
lista = []

for i in range(10):
    numeros = int(input(f'Digite o {i + 1}º número: '))
    lista.append(numeros)
print(f'O menor valor é = {min(lista)}')
print(f'O maior valor é = {max(lista)}')
print(f'A soma dos valores é = {sum(lista)}')
