###### FOR - WHILE  #####

# Escreva um código que conte de 10 até 0 com um intervalo de 1 segundo e mostre no final FELIZ ANO NOVO!


# from time import sleep

# for cont in range(10,0,-1):
#     print(cont, end= ' ')
#     sleep(1)
# print('\nFeliz Ano Novo!')

#### USANDO WHILE ####
# from time import sleep

# cont = 10
# while cont != 0:
#     print(cont, end = ' ')
#     sleep(1)
#     cont -= 1
# print('\nFeliz ano novo')

# for c in range(1,4):
#     n= int(input('Digite um número: '))
# print('fim')

# n = 1
# while n !=0:
#     n = int(input('Digite um número: '))

# print('Fim')

# n = 0 
# r = 'S'
# while r =='S': #Enquanto a variavel 'r' for verdadeira 'S', continue  o laço
#     n = int(input('Digite um valr'))
#     r = input('Quer continuar? [S/N]').upper()
# print('fim')

# n = 1
# par = impar = 0
# while n !=0:
#     n = int(input('Digite um valor: '))
#     if n != 0:
#         if n % 2 == 0:
#             par +=1
#         else:
#             impar +=1

# print(f'Digitou {par} número pares e {impar} números impares!')


# 
# n = s = 0
# while True: #LAÇO infinito até o BREAK
#     n = int(input('Digite um numero: '))
#     if n == 999:
#         break
#     s += n
# print(f'A soma é {s}')

from random import randint

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador

    tipo = ' '

    while tipo not in 'PI':
        tipo = input('Par ou Impar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total foi {total}')

    if tipo =='P':
        if total % 2 == 0:
            print('Você venceu!')
            v +=1
        else:
            print('kkkkkk VOCÊ PERDEU')
            break
    elif tipo =='I':
        if total % 2 !=0:
            print('Você venceu!')
            v += 1
        else:
            print('kkkkk VOCê PERDEU')
            break

    print('\nVamos jogar novamente')
print(f'GAMER OVER! Você venceu {v} vezes.')