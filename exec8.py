# 8. Faça um programa que leia 5 números e informe a soma
# e a média dos números.

lista = []

while len(lista) < 5:
    lista.append(int(input(f'Digite o {len(lista) + 1}º número: ')))
print(f'A soma dos números da lista é = {sum(lista)}')
print(f'A média dos números é = {sum(lista) / len(lista)}')
