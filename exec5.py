# 5. Altere o programa anterior permitindo ao usuário informar
# as populações e as taxas de crescimento iniciais. Valide a
# entrada e permita repetir a operação.

popA = float(input('Digite a quantidade populacional PAÍS A:  '))
popB = float(input('Digite a quantidade populacional PAÍS B:  '))
taxa_A = float(input('Informe a taxa de crescimento do PAÍS A:  '))
taxa_B = float(input('Informe a taxa de crescimento do PAÍS B:  '))
ano = 0
print('============================================================')
print('Crescimento da população A em relação a população B')
print(f'População A = {popA} habitantes e cresce 3% ao ano')
print(f'População B = {popB} habitantes e cresce 1.5% ao ano')
while popA <= popB:
    popA += ((popA * taxa_A) / 100)
    popB += ((popB * taxa_B) / 100)
    ano += 1

print(f"a população A irá ultrapassar ou igualar a população B em {ano} anos")
