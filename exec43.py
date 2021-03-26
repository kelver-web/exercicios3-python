# 43. O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e
# as quantidades desejadas. Calcule e mostre o valor a ser
# pago por valor (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

from colorama import Fore, init
init(convert=True)


print(Fore.YELLOW + '''CARDÁPIO =============== CÓDIGO === PREÇOS
Cachorro Quente -------- 100 -------R$ 1.20
Bauru Simples ---------- 101 -------R$ 1.30
Bauru com Ovo ---------- 102 -------R$ 1.50
Hambúrguer ------------- 103 -------R$ 1.20
Cheeseburguer ---------- 104 -------R$ 1.30
Refrigerante ----------- 105 -------R$ 1.00''', Fore.WHITE)


codigos = [100, 101, 102, 103, 104, 105]
pedido = 1
soma = 0

while True:
    print(f'\nPEDIDO Nº {pedido}')
    codigo = int(input('INFORME O CODIGO:   '))

    while codigo not in codigos:
        print('CÓDIGO INVÁLIDO!')
        codigo = int(input('INFORME O CODIGO CORRETO:   '))
    quant = int(input('INFORME A QUANTIDADE:   '))
    continua = input('CONTINUE [S] OU [N]:  ')
    pedido += 1

    if codigo == 100:
        valor = quant * 1.20
        soma += valor
        print(f'CÓDIGO: {codigo} --- CACHORRO QUENTE ---> R${valor:.2f}')
        if continua in 'Nn':
            break

        else:
            continue

    elif codigo == 101:
        valor = quant * 1.30
        soma += valor
        print(f'CÓDIGO: {codigo} --- BAURU SIMPLES ---> R${valor:.2f}')
        if continua in 'Nn':
            break

        else:
            continue

    elif codigo == 102:
        valor = quant * 1.50
        soma += valor
        print(f'CÓDIGO: {codigo} --- BAURU COM OVO ---> R${valor:.2f}')
        if continua in 'Nn':
            break

        else:
            continue

    elif codigo == 103:
        valor = quant * 1.20
        soma += valor
        print(f'CÓDIGO: {codigo} --- HAMBURGUER ---> R${valor:.2f}')
        if continua in 'Nn':
            break

        else:
            continue

    elif codigo == 104:
        valor = quant * 1.30
        soma += valor
        print(f'CÓDIGO: {codigo} --- CHEESEBURGUER ---> R${valor:.2f}')
        if continua in 'Nn':
            break

        else:
            continue

    elif codigo == 105:
        valor = quant * 1.00
        soma += valor
        print(f'CÓDIGO: {codigo} --- REFRIGERANTES ---> R${valor:.2f}')
        if continua in 'Nn':
            break

        else:
            continue
print()
print(Fore.RED + f'TOTAL DO PEDIDO ---> R${soma:.2f}')
print('OBRIGADO E VOLTE SEMPRE!')
