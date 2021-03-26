# 17. Faça um programa que calcule o fatorial de um
# número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

print('Digite um número negativo para sair')
n = int(input('Digite um número inteiro positivo:  '))
while n >= 0:
    fatorial = 1

    while n > 1:
        fatorial *= n
        n -= 1
    print(fatorial)
    n = int(input('Digite um número inteiro positivo:  '))
print('Finalizado')
