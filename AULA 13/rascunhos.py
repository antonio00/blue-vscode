#### DICIONARIOS ###
# () tuplas, listas [], {} dicionarios

# dados = dict() # cria dicionario vazio
# dados ={'nome': 'Thiago', 'idade': 27}

# print(dados['nome'])

# print(dados['peso']) # esse print de chave que nao existe retornará None e um erro chamado KeyError

#para tratar esse erro usa o get.
# if dados.get('peso') == None:# o get vasculha o dicionario em busco de "chaves" qu nao existe
#    dados.setdefault('peso', 70) #add um valor padrao a chave que nao existe
#    print('peso não existe') 
    
# else:
#     print(dados['peso'])


# print(dados)

###### VALUE() KEYS(), ITENS()
# musica = {
#     'nome': 'Leave the door open',
#     'autor': 'Bruno Mars',
#     'lancamento': 2021
# }

# print(musica.values())
# print(musica.keys())
# print(musica.items())

# for k in musica.keys():
#     print(k)
# for v in musica.values():
#     print(v)
# for k, v in musica.items():
#     print(f'O {k} é {v}')

# musica1 = {
#     'nome': 'Leave the door open',
#     'autor': 'Bruno Mars',
#     'lancamento': 2021
# }

# musica2 = {
#     'nome': 'Empire estate of mind',
#     'autor': 'Alicia Keys',
#     'lancamento': 2009
# }

# musica3 = {
#     'nome': 'Paradise',
#     'autor': 'ColdPlay',
#     'lancamento': 2011
# }

# deezer = list()

# deezer.append(musica1)
# deezer.append(musica2)
# deezer.append(musica3)

# print(deezer[0]['autor'])

# pessoa = dict()
# povo = list()

# for c in range(0,3):
#     pessoa['nome'] = str(input('Nome:'))
#     pessoa['idade'] = int(input('Idade: '))

#     povo.append(pessoa.copy()) #cria uma copia do dicionario dentro da lista

# print(povo)
# for p in povo:
#     for v in p.values():
#         print(v, end=' ')
#     print()

# Faca um progama que leia  nome e media de um aluno, guardando tambm a situacao em um dicionario.
    #no final, mostre o conteudo da estrutura da tela

# aluno = dict()
# aluno['nome'] = str(input('Nome: '))
# aluno['media'] =  float(input(f'Média de {alno["nome"]}'))

# if aluno['media'] >= 7:
#     aluno['situacao'] = 'Aprovado'
# elif 5 <= aluno['media'] <7:
#     aluno['situacao'] = 'Recurepação'
# else:
#     aluno['situcao'] = 'FERROU! REPROVADO'
#     print()
# for k, v in aluno.items():
#     print(f'{k} é igual a {v}')

#

from random import randint
from time import sleep
from operator import itemgetter
jogo ={
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
ranking = dict()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('='*30)
print('O ranking de vencedores é: ')
print('='*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print('==========DADO DO ÓDIO==========')
