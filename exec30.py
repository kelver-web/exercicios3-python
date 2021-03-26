# 30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e
# pretende implantar a metodologia da tabelinha, que já é um
# sucesso na sua loja de 1,99. Você foi contratado para desenvolver
# o programa que monta a tabela de preços de pães, de 1 até 50 pães,
# a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

from colorama import Fore, init
init(convert=True)

lista = []
pao = 1
valor = 0.18

print(Fore.GREEN + '==== PADARIA DO SR. MANOEL JOAQUIM ====', Fore.WHITE)

while pao <= 50:
    print(f'{pao} --- uni. Pão(es) ----> R${pao * valor:.2f}')
    pao += 1

for i in range(pao):
    i = int(input('Digite quantos pães você deseja levar:  '))
    lista.append(i)
    print(Fore.RED + f'{i} -- Pão(es) irá custar ----> R${i * valor:.2f}', Fore.WHITE)
    break
