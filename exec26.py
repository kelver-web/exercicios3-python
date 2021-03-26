# 26. Numa eleição existem três candidatos. Faça um programa
# que peça o número total de eleitores. Peça para cada eleitor
# votar e ao final mostrar o número de votos de cada candidato.
from colorama import Fore, init
init(convert=True)


luiz = 0
fernando = 0
jair = 0

print('''=== CANDIDATOS ===
[A] LUIS INÁCIO
[B] FERNANDO HENRIQUE
[C] JAIR BOLSONARO''')
eleitores = int(input('Informe a quantidade de eleitores: '))

for i in range(eleitores):
    voto = input(f'{i + 1}º  Candidato Informe seu voto pela letra:  ')
    if voto in 'Aa':
        luiz = luiz + 1
    elif voto in 'Bb':
        fernando = fernando + 1
    elif voto in 'Cc':
        jair = jair + 1

print(Fore.GREEN, f'O candidato LUIZ INÁCIO teve ---------> {Fore.RED + str(luiz)}\
 votos')
print(Fore.BLUE, f'O candidato FERNANDO HENRIQUE teve ---> {Fore.RED + str(fernando)}\
 votos')
print(Fore.YELLOW, f'O candidato JAIR BOLSONARO teve ------> {Fore.RED + str(jair)}\
 votos')
# Aqui eu quis colocar uma cor diferente com o pacote colorama
