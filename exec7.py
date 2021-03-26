# 7 . Faça um programa que leia 5 números e informe o maior número.

lista = []

while len(lista) < 5:
    lista.append(input(f'Digite o {len(lista) + 1}º número: '))
print(f'O maior número da lista é {max(lista)}')
