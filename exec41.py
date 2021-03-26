# 41. Faça um programa que receba o valor de uma dívida e mostre
# uma tabela com os seguintes dados: valor da dívida, valor dos
# juros, quantidade de parcelas e valor da parcela.
'''Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67'''

from colorama import Fore, init
init(convert=True)

divida = float(input('Digite o valor da sua divida:  '))
parcela = 1
print()
print(Fore.YELLOW + 'Valor da divida: ', end=' ')
print('Valor do juros: ', end=' ')
print('Quantidade de parcelas: ', end=' ')
print('Valor da parcela:', Fore.WHITE)

for i in range(5):
    if parcela == 1:
        juros = 1
        v_juros = 0
    elif parcela == 4:
        parcela = 3
        juros = 1.10
    elif parcela == 7 or parcela == 6:
        parcela = 6
        juros = 1.15
    elif parcela == 10 or parcela == 9:
        parcela = 9
        juros = 1.20
    elif parcela == 13 or parcela == 12:
        parcela = 12
        juros = 1.25

    v_juros = divida * (juros - 1)
    div_juros = divida * juros
    v_parcela = div_juros / parcela

    print(f'R$ {div_juros:.2f}', end=' ------------ ')
    print(f'{v_juros:.2f}', end=' ----------------- ')
    print(f'{parcela}', end=' ----------------- ')
    print(f'R$ {v_parcela:.2f}')
    parcela += 3
