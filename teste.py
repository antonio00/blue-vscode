pessoas = list()
pessoa = dict() #criei meu dicionario pessoa
maiorIdade = 0
homem = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = input('Nome: ')
    while True:
        pessoa['Sexo'] = input('Sexo: [M/F]').upper()[0]
        if pessoa['Sexo'] == 'M':
            homem += 1
        if pessoa['Sexo'] in 'MF':
            break
        print('Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    if pessoa['idade'] > 18:
        maiorIdade += 1
    pessoas.append(pessoa.copy())
    while True:
        resposta = input('Quer continuar? [S/N]').upper()[0]
        if resposta in 'SN':
            break
        print('Responda apenas S ou N')
    if resposta =='N':
        break

print('*'*35)
print(f'Temos {maiorIdade} maior de idade.')
print(f'Temos {homem} homem/homens cadastrados.')

