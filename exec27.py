# 27. Faça um programa que calcule o número médio de alunos
#  por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter
# mais de 40 alunos.
from colorama import Fore, init
init(convert=True)


lista = []

turma = int(input('Digite a quantidade de turmas: '))

for i in range(turma):
    alunos = int(input(f'Digite a quantidade de alunos da {i + 1}º turma:  '))
    lista.append(alunos)
    soma = sum(lista)
    media = soma / len(lista)

if media > 40:
    a = media
    print(Fore.RED, f'{a:.0f} ultrapassa a média de alunos por turma')
else:
    print(Fore.YELLOW, f'A média da alunos por turma é = {media:.0f}')
