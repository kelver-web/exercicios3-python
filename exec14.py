# 14. Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a
# quantidade de números impares.


pares = 0
impares = 0

lista = []
for n in range(1, 11):
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)

    if numero % 2 == 0:
        pares += 1

    else:
        impares += 1
print()
print('Mostrando a lista de números')
print(lista)
print(f'Total de números Pares = {pares}')
print(f'Total de números Ímpares = {impares}')
