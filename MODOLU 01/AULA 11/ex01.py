#programa que leia nome e peso de varias pessoas, guardando em lista. pergunte o usuario se quer continuar
# nao querendo continuar, pare o programa
# quantas pessoas cadastradas
# maior peso
# menor peso

dados = list() # lista temporaria
nome = list() # lista principal
maior = menor = 0

while True: 
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(nome) == 0: #verifica se lista "nome" esta vazia ou nao
        maior = menor = dados[1]
    else:
        if dados[1] > maior: # se indice 1 da lista dados for maior que a variavel maior
            maior = dados[1] # entao variavel maior recebe o valor digitado
        if dados[1] < menor: # se for menor, a variavel menor recebe
            menor = dados[1]
    
    nome.append(dados[:])#add dados da lista "dados" na lista "nome"
    dados.clear() # limpa a lista temporaria para receber o proximo
    resposta = str(input('Quer Continuar? [S/N]'))
    if resposta in 'Nn':
        break

print('*'*40)
print(f'Você cadastrou: {len(nome)} pessoas')
print(f'O maior peso foi {maior}kg.')
print(f'O menor peso foi {menor}kg.')
print('********* Desenvolvido Por AML********')