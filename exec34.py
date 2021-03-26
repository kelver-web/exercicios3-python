# 34. Os números primos possuem várias aplicações dentro da Computação,
# por exemplo na Criptografia. Um número primo é aquele que é divisível
# apenas por um e por ele mesmo. Faça um programa que peça um número
# inteiro e determine se ele é ou não um número primo.

from colorama import Fore, init
init(convert=True)

print(Fore.GREEN + '/=' * 20)
print('/    NÚMEROS PRIMOS E NÃO PRIMOS      /')
print('/=' * 20, Fore.WHITE)

num = int(input('Digite um número:  '))

if num % 2 == 1:
    print(Fore.YELLOW + f'{num}-> É primo')
else:
    print(Fore.RED + f'{num}-> Não é primo')