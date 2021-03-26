# 21. Faça um programa que peça um número inteiro e determine
# se ele é ou não um número primo. Um número primo é aquele
# que é divisível somente por ele mesmo e por 1.


num = int(input('Digite um número:  '))

if num % 2 == 1:
    print(f'{num}-> É primo')
else:
    print(f'{num}-> Não é primo')
