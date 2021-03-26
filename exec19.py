# 19. Altere o programa anterior para que ele aceite apenas
# números entre 0 e 1000.


lista = []
cont = 0

quant = int(input('Escolha quantos números deseja digitar:  '))
while quant != cont:
    numero = int(input(f'Digite {cont + 1}º número: '))

    while numero > 1000 or numero < 0:
        numero = int(input('Digite um número entre 0 e 1000:  '))

    lista.append(numero)
    cont += 1

print(f'Lista: {lista}')
print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')
print(f'A soma dos valores é = {sum(lista)}')
