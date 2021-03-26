# 25. Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
# dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

idade_pessoas = int(input('Quantas pessoas irá intrevistar?  '))
lista = []
for i in range(idade_pessoas):
    pessoa = int(input(f'Digite a idade da {i + 1}º pessoa:  '))
    lista.append(pessoa)
    soma = sum(lista)
    media = soma / len(lista)
print(f'VOCÊ DIGITOU A(S) IDADE(S) {lista}')

if media <= 25.26 and media >= 0:
    print(f'Média de idade é {media} anos, essa turma é jovem')
elif media > 25.26 and media <= 60:
    print(f'Média de idade é {media} anos, essa turma é adulta')
elif media > 60:
    print(f'A média de idade é {media} anos, essa turma é idosa')
