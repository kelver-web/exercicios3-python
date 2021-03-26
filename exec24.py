# 24. Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input('Quantas notas gostaria de ver?  '))

lista = []
for i in range(n):
    nota = float(input(f'Digite a {i + 1}º nota:  '))
    lista.append(nota)
    
print(f'Você digitou as notas {lista}')
print(f'A média aritimética das notas é = {sum(lista) / len(lista)}')
