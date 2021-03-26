# 6 . Faça um programa que imprima na tela os números de 1 a 20,
# um abaixo do outro. Depois modifique o programa para que ele
# mostre os números um ao lado do outro.

print('Mostrando os números um abaixo do outro')
num = 1
while num < 21:
    print(num)
    num += 1
# OBS: quando eu coloco o print já no início é uma coisa,
# quando coloco o print no final é outra coisa

print('Mostrando os números um ao lado do outro')
num = 0
while num < 20:
    num += 1
    print(num, end=', ')
