# 15. A série de Fibonacci é formada pela seqüência
# 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz
# de gerar a série até o n−ésimo termo.

anterior = 0
seguinte = 1

fibonacci = []

quant = int(input('Quantos termos você gostaria de ver?  '))
for i in range(quant):
    fibonacci.append(anterior)
    anterior, seguinte = seguinte, anterior + seguinte

for num in fibonacci:
    print(num, end=', ')
# Só quis retirar a sequência de dentro da lista.
