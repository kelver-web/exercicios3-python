# 16. A série de Fibonacci é formada pela seqüência
# 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que
# gere a série até que o valor seja maior que 500.

quant = 16
anterior = 0
seguinte = 1

fibonacci = []

for i in range(quant):
    fibonacci.append(anterior)
    anterior, seguinte = seguinte, anterior + seguinte

for num in fibonacci:
    print(num, end=', ')
# Só quis retirar a sequência de dentro da lista.
