#Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. 
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
print('='*30)
print('Bem vindo a mais uma ferramenta Blue')
print('='*30)
senha = '5467'
tentativa=input("Digite a senha:")
rodadas = 1
while senha != tentativa:
    print("Senha Incorreta! Tente novamente!")
    tentativa=input("Digite a senha:")
print("Senha correta. Acesso liberado...")
sleep(2)
maquina = randint (0,10) # "Computador pensa"
print('-' * 25) # printa 25 caracter '-'
print('Irei escolher um número entre 0 e 10. Tente acertar! ')
print('-' * 25)
pessoa = int(input('Qual número eu pensei? ')) # Recebe valor do jogador(pessoa)
while pessoa != maquina:
    print('Errou! Tente novamente')
    if pessoa > maquina:
        print('Tente um número mais baixo')
    else:
        print('Tente um número mais alto')
    pessoa = int(input('Qual número eu pensei? '))
    rodadas += 1 # sempre que for digitado outro numero é somado +1 a variavel rodadas
print('='*30)
if pessoa == maquina:
    print('Parabén você acertou')
print(f'Foram necessárias {rodadas} tentativas para acertar!')
