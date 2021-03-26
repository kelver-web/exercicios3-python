# 2. Faça um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário, mostrando uma
# mensagem de erro e voltando a pedir as informações.

nome = input('Digite o seu nome: ')
senha = input('Digite a sua senha: ')

while nome == senha:
    print('Nome e senha iguais, por favor digite novamente.')
    nome = input('Digite o seu nome: ')
    senha = input('Digite a sua senha: ')

print(nome, senha)
