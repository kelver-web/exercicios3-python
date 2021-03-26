# 35. Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos
# existentes entre 1 e um número inteiro informado pelo usuário.

from colorama import Fore, init
init(convert=True)

lista = []

print(Fore.GREEN + '/=' * 20)
print('/    LISTA DE NÚMEROS PRIMOS      /')
print('/=' * 20, Fore.WHITE)

num = int(input('Digite um número:  '))


for i in range(1, num):
    if i % 2 == 1:
        lista.append(i)
print(Fore.YELLOW + f'PRIMOS = {lista}')
