#Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. 
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.



from random import randint
maquina = randint (0,10) # "Computador pensa"
print('-' * 25) # printa 25 caracter '-'
print('Irei escolher um número entre 0 e 10. Tente acertar! ')
print('-' * 25)
pessoa = int(input('Qual número eu pensei? ')) # Recebe valor do jogador(pessoa)
print ('Pensei o número {}'.format(maquina))
if pessoa == maquina:
    print('Parabén você acertou')
else:
    print(f'Eu venci! Pensei no número {maquina}')

