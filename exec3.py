# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Digite o seu nome:  '))
while (len(nome) <= 3):
    print('Seu nome tem que ter mais de três letras')
    nome = str(input('Digite o seu nome:  '))

idade = int(input('Digite a sua idade:  '))
while idade < 0 or idade > 150:
    print('Digite a sua idade corretamente.')
    idade = int(input('Digite a sua idade:  '))


salario = float(input('Digite o seu salário:  '))
while salario <= 0:
    print('Digite o salário correto')
    salario = float(input('Digite o seu salário:  '))


print('''== Sexo ==
[M] - Masculino
[F] - Feminino''')
sexo = input('Digite o seu sexo:  ')
while sexo not in 'Mm, masculino' and sexo not in 'Ff, feminino':
    print('Informe o sexo corretamente.')
    sexo = input('Digite o seu sexo:  ')


print('''== Estado Civil ==
[S] - Solteiro
[C] - Casado
[V] - Viúvo
[D] - Divorciado''')
estado_civil = input('Digite o seu estado civil:  ')
while estado_civil not in 'Ss, solteiro, Cc, casado, Vv, viuvo, Dd, divorciado':
    print('Digite o seu estado civil corretamente')
    estado_civil = input('Digite o seu estado civil:  ')
print('|=========================================|')
print('|        Informações sobre o usuário      |')
print(f'|Nome ----------> {nome}                  |')
print(f'|Idade ---------> {idade} anos                 |')
print(f'|Salário -------> R${salario}                |')
print(f'|Sexo ----------> {sexo}               |')
print(f'|Estado civil --> {estado_civil}                  |')
print('|=========================================|')
