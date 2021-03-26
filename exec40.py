# 40. Foi feita uma estatística em cinco cidades brasileiras para coletar
# dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos
# de passeio.

codigo_cidade = []
n_veiculo = []
n_acidente = []
n_acidente_2000 = []

print('### ESTATÍSTICAS SOBRE ACIDENTE DE TRÂNSITO NO BRASIL ###')
for i in range(5):
    print(f'\n{i + 1}º CIDADE:')
    codigo = int(input('Código da cidade:  '))

    while codigo in codigo_cidade:
        print('Código já informado.')
        codigo = int(input('Digite outro código:  '))

    veiculos = float(input('Número de veículos:  '))
    acidentes = float(input('Acidentes:  '))

    if veiculos > 2000:
        n_acidente_2000.append(acidentes)
        n_acidente.append(acidentes)
    else:
        n_acidente.append(acidentes)

    n_veiculo.append(veiculos)
    codigo_cidade.append(codigo)


maior_acidente = n_acidente.index(max(n_acidente))
menor_acidente = n_acidente.index(min(n_acidente))

media_veiculos = sum(n_veiculo) / len(n_veiculo)
media_acidentes = sum(n_acidente_2000) / len(n_acidente_2000)

print()
print('MEMOS ACIDENTES')
print(f'Quantidade de acidentes: {min(n_acidente)}')
print(f'Código da cidade: {codigo_cidade[menor_acidente]}')
print()
print('MAIS ACIDENTES')
print(f'Quantidade de acidentes: {max(n_acidente)}')
print(f'Código da cidade: {codigo_cidade[maior_acidente]}')
print()
print(f'MÉDIA DE VEÍCULOS NAS 5 CIDADES: {media_veiculos}')
print(f'MÉDIA DE ACIENTES NAS CIDADES COM MENOS DE 2000 VEÍCULOS: \
{media_acidentes}')
