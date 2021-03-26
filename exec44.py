# 44. Em uma eleição presidencial existem quatro candidatos. Os votos são
# informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o
# conjunto de votos tem-se o valor zero.


print('''===== ELEIÇÃO PRESIDENCIAL =====
[1] LUÍS INÁCILO LULA DA SILVA
[2] JAIR BOSSONARO
[3] CIRO GOMES
[4] LUCIANO HULK
[5] NULO
[6] BRANCO''')

n_candidatos = [1, 2, 3, 4, 5, 6]

candidatos = ['Luis inacio lula da silva',
              'Jair Bolsonaro',
              'Ciro gomes',
              'Luciano hulk',
              'Nulo',
              'Branco']
votos = []
n_votos = 1
voto = True

while voto != 0:
    print(f'VOTO Nº {n_votos}')
    voto = int(input('INFORME O SEU VOTO:  '))
    n_votos += 1

    while voto not in n_candidatos:
        print('VOTO INVÁLIDO!')
        voto = int(input('INFORME O SEU VOTO PELA LEGENDA:  '))
    continua = input('DESEJA CONTINUAR [S] SIM, [N] NÃO:  ')
    votos.append(voto)

    if continua in 'Ss':
        continue
    else:
        break


print()
for i in range(len(candidatos)):
    print(f'VOTOS PARA ------> {candidatos[i]}', end=" = ")
    if votos.count == 0:
        print('0')
        i += 1
    else:
        print(votos.count(i + 1))
        i += 1

p_nulo = (votos.count(5) / len(votos)) * 100
p_branco = (votos.count(6) / len(votos)) * 100
print(f'NULOS -----------> {p_nulo:.2f}%')
print(f'BRANCO ----------> {p_branco:.2f}%')
