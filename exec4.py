# 4. Supondo que a população de um país A seja da ordem de 80000
# habitantes com uma taxa anual de crescimento de 3% e que a
# população de B seja 200000 habitantes com uma taxa de crescimento
# de 1.5%. Faça um programa que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale
# a população do país B, mantidas as taxas de crescimento.

popA = 80000
popB = 200000
ano = 0

print('Crescimento da população A em relação a população B')
print(f'População A = {popA} habitantes e cresce 3% ao ano')
print(f'População B = {popB} habitantes e cresce 1.5% ao ano')
while popA <= popB:
    popA += popA * 0.03
    popB += popB * 0.015
    ano += 1

print(f"a população A irá ultrapassar ou igualar a população B em {ano} anos")
