galera = list()
dados = list()
totalMaior = TotalMenor = 0

for c in range(0,3):
    # dados = list() pode ser usada assim tambem em substituicao do dados.clear
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear() # apos add dados em galera, limpa os dados e refaz o range.

for g in galera:
    if g[1] >= 18:
        print(f'{g[0]} é maior de idade')
        totalMaior += 1
    else:
        print(f'{g[0]} é menor de idade')
        TotalMenor +=1
print(f'Temos{totalMaior} maiores e {TotalMenor} menores de idade')