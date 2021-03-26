# 37. Uma academia deseja fazer um senso entre seus clientes
# para descobrir o mais alto, o mais baixo, a mais gordo e o
# mais magro, para isto você deve fazer um programa que pergunte
# a cada um dos clientes da academia seu código, sua altura e seu peso.
# O final da digitação de dados deve ser dada quando o usuário
# digitar 0 (zero) no campo código. Ao encerrar o programa também
# deve ser informados os códigos e valores do clente mais alto,
# do mais baixo, do mais gordo e do mais magro, além da média das
# alturas e dos pesos dos clientes

from colorama import Fore, init
init(convert=True)

lista = []
cliente = 1
cod = True

while cod != 0:
    print(f'\nCliente nº {cliente}')
    codigo = int(input('Informe seu código:  '))
    if codigo == 0:
        break
    else:
        altura = float(input('Qual é a sua altura:  '))
        peso = float(input('Qual é o seu peso:  '))
        print('DIGITE [0] PARA SAIR.')
        lista.append(codigo)
        lista.append(altura)
        lista.append(peso)
        cliente += 1

        codigos = lista[0::3]
        alturas = lista[1::3]
        pesos = lista[2::3]
        media_altura = (sum(alturas) / len(alturas))
        media_peso = (sum(pesos) / len(pesos))

print(Fore.GREEN + f'OS CÓDIGOS INFORMADOS FORAM = {codigos}')
print(f'O CLIENTE MAIS ALTO TEM ----> ALTURA: {max(alturas):.2F} METROS')
print(f'O CLIENTE MAIS BAIXO TEM ---> ALTURA: {min(alturas):.2f} METROS')
print(f'O CLIENTE MAIS GORDO TEM ---> PESO: {max(pesos):.2f} Kg')
print(f'O CLIENTE MAIS MAGRO TEM ---> PESO: {min(pesos):.2f} Kg')
print(f'A MÉDIA DE ALTURA É DE -----> MÉDIA ALTURA: {media_altura:.2f} METROS')
print(f'A MÉDIA DE PESO É DE -------> MÉDIA PESO: {media_peso:.2f} Kg')

