# 20. Altere o programa de cálculo do fatorial,
# permitindo ao usuário calcular o fatorial várias vezes e
# limitando o fatorial a números inteiros positivos
# e menores que 16.

while True:
    n = int(input('informe um número:  '))
    print(f'{n}! Fatorial')
    fatorial = 1
    if n > 16 or n < 0:
        print('Número incorreto tente novamente:')
    else:
        while n > 1:
            fatorial *= n
            n -= 1
        print(f'Resultado = {fatorial}')
    print('Digite [-1] para sair')
    if n == - 1:
        break
print('Finalizado')
