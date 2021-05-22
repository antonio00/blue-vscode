# 4.	Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. 
# No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. 
# Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.

from random import randint
from time import sleep
from operator import itemgetter
jogo ={                                 #dicionario jogo, com 4 chaves, 'jogador1,2,3,4'
    'jogador1': randint(1,6),           # valores da chaves seram randomicos, entre 1 e 6. pois dado tem 6 lados
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
ranking = dict() # cria outro dicionario para poder criar o ranking
print('Valores sorteados: ')
for k, v in jogo.items(): # for vai vasculhar keys e value em items do dic jogos
    print(f'{k} tirou {v}') # printa keys(nomes dos jogadores(k)) e value(v) -
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # sorted organiza dic,  de acordo com items(), usa itemgetter, para referencia
print('='*30)
print('O ranking de vencedores é: ')
print('='*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print('==========DADO DO ÓDIO==========')