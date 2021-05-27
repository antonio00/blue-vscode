# Crie uma classe chamada Conta para simular as operações de uma conta corrente.
#  Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. 
# Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ 
# Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, 
# caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."

from conta import Conta

nome = str(input('Digite o nome do titular: '))
c1 = Conta(nome)

saque = float(input('Digite o valor do saque: R$'))
c1.saque(saque)

