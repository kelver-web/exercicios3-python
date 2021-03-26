# 39. Faça um programa que leia dez conjuntos de dois valores,
# o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno
# mais alto e o mais baixo. Mostre o número do aluno mais alto e
# o número do aluno mais baixo, junto com suas alturas.

from colorama import Fore, init
init(convert=True)


numero_alunos = []
altura_alunos = []

for i in range(2):
    print(f'\n{i + 1}º Aluno:')
    n_aluno = int(input('Número do aluno:  '))
    while n_aluno in numero_alunos:
        print('=== Númro já informado ===')
        n_aluno = int(input('Digite outro número:  '))
    altura_alunos.append(float(input('Digite a altura do aluno: ')))
    numero_alunos.append(n_aluno)

baixo = altura_alunos.index(min(altura_alunos))
alto = altura_alunos.index(max(altura_alunos))
print()
print(Fore.YELLOW + '=====================')
print('INFORMAÇÕES DO ALUNO')
print('=====================', Fore.WHITE)
print()
print(Fore.BLUE + '### Aluno mais baixo ###')
print(f'Número ---> {numero_alunos[baixo]}')
print(f'Altura ---> {min(altura_alunos)}', Fore.WHITE)
print()

print(Fore.GREEN + '### Aluno mais alto ###')
print(f'Número ---> {numero_alunos[alto]}')
print(f'Altura ---> {max(altura_alunos)}')
