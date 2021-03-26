# 47. Em uma competição de ginástica, cada atleta recebe votos
# de sete jurados. A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes. Você deve
# fazer um programa que receba o nome do ginasta e as notas dos
# sete jurados alcançadas pelo atleta em sua apresentação e depois
# informe a sua média, conforme a descrição acima informada
# (retirar o melhor e o pior salto e depois calcular a média com as
# notas restantes). As notas não são informados ordenadas. Um exemplo
# de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04



nome_ginasta = True
n_ginasta = 1
notas = []

while nome_ginasta != '':
    nome_ginasta = input('ATLETA:  ')

    if nome_ginasta == '':
        break
    else:
        for i in range(7):
            nota = float(input('NOTA:  '))
            notas.append(nota)

        melhor = max(notas)
        pior = min(notas)
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        print('=======================')
        print('RESULTADO FINAL:')
        print(f'ATLETA: {nome_ginasta}')
        print(f'MELHOR NOTA: {melhor}')
        print(f'PIOR NOTA: {pior}')
        print(f'MÉDIA: {media}')
