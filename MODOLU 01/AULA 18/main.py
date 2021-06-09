# Crie uma classe chamada Conta para simular as operações de uma conta corrente.
#  Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. 
# Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ 
# Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, 
# caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."

from conta import Conta

titular = str(input('Digite o nome do titular: '))
c1 = Conta(titular)

while True:
    opcao = int(input('''
        O que deseja fazer:
        [ 1 ] Sacar
        [ 2 ] Depositar
        [ 3 ] Saldo
        [ 4 ] Sair
    '''))
    resp = ' '
    if opcao == 1:
        while True:
            saque = float(input('Digite valor que deseja sacar: R$ '))
            c1.saque(saque)
            resp = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
            if resp == 'N':
                break

    elif opcao == 2:
        while True:
            deposito = float(input('Digite o valor que deseja deposiar: R$ '))
            c1.deposito(deposito)
            resp = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
            if resp == 'N':
                break

    elif opcao == 3:
        while True:
            c1.extrato()
            resp = str(input('Retornar Menu principal? [S/N]: ').strip().upper()[0])
            if resp == 'S':
                break

    elif opcao == 4:
        print('Transação finalizada!')
        print('Volte sempre')
        break

    else:
        print('Opção inválida')
    



        