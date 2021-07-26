#01 - Crie um programa que leia dois valores e mostre um menu na tela:
   # [ 1 ] somar
   # [ 2 ] multiplicar
   # [ 3 ] maior
   # [ 4 ] novos números
   # [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

from time import sleep

num1  = int(input('Digite primeiro número: '))
num2  = int(input('Digite segundo número: '))
opcao = 0
while opcao != 5: 
    #aspas triplas no print, mostra o texto conforme eu escrevir no codigo.
    print('''    [1] Somar  
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao =int(input('O que deseja fazer: '))
    if opcao == 1:
        soma = num1 + num2
        print(f'O resultado da sua soma {num1} + {num2} é de: {soma}')

    elif opcao == 2:    
        multi = num1 * num2
        print(f'O resultado da sua multiplicação {num1} * {num2} é de: {multi}')

    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Maior valor entre {num1} e {num2} é {maior}')
    elif opcao == 4:
        print('Comece novamente!')
        num1  = int(input('Digite primeiro número: '))
        num2  = int(input('Digite segundo número: '))

    elif opcao == 5:
        print('Programa encerrado')
        print()
        print('============Desenvolvido a base de ódio============')
    else:
        print('Opção inválida. Digite uma das opções listada!')
    sleep(3)
    print()

