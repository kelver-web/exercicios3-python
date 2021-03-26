# 45. Desenvolver um programa para verificar a nota do aluno em uma
# prova com 10 questões, o programa deve perguntar ao aluno a resposta
# de cada questão e ao final comparar com o gabarito da prova e assim
# calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo
# que o professor digite o gabarito da prova antes dos alunos
# usarem o programa.


gabarito = []
res_alunos = []
notas_tiradas = []

print('\nGABARITO DO PROFESSOR:')
for i in range(10):
    print(f'{i + 1}º QUESTÃO:  ')
    resposta_certa = gabarito.append(input('QUAL É A ALTERNATIVA CORRETA:  '))

n_aluno = 1
continuar = True
aluno = []

while continuar != 'n':
    print()
    print(f'ALUNO Nº {n_aluno}')
    n_aluno += 1
    alunos = input('DIGITE O SEU NOME:  ')
    print(f'OLÁ {alunos}, VOCÊ JÁ PODE INICIAR A SUA PROVA')
    res_alunos.clear()
    aluno.append(alunos)

    for i in range(10):
        print(f'QUESTÃO: {i + 1}')
        resposta_aluno = res_alunos.append(input('ESCOLHA UM ALTERNATIVA:  '))
    nota = 0

    for i in range(10):
        if res_alunos[i] == gabarito[i]:
            nota += 1
    notas_tiradas.append(nota)
    continuar = input('ALUNO, IRÁ UTILIZAR O SISTEMA [S] SIM [N] NÃO:  ')

print()
print(f'{len(notas_tiradas)} ALUNO(S) USOU(ARAM) O SISTEMA')
print(aluno)
print(f'A MAIOR NOTA FOI: {max(notas_tiradas)}')
print(f'A MENOR NOTA FOI: {min(notas_tiradas)}')
print(f'A MÉDIA DA TURMA FOI: {sum(notas_tiradas) / len(notas_tiradas)}')
print(notas_tiradas)
