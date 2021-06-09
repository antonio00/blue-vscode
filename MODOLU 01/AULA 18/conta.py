class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo # o underline2x torna o valor de saldo privado.
        
    
    def saque(self,valorS):
        if valorS != 0:
            if self.__saldo >= valorS:
                self.__saldo -= valorS
                print(f'Saque de R${valorS} autorizado!')
                print(f'Seu novo saldo é de: R$ {self.__saldo}')
            else:
                print(f'Saque R${valorS} não autorizado!')
                print(f'Saldo insunficiente! Saldo disponivel R${self.__saldo}')
    
    def deposito(self, valorD):
        self.__saldo += valorD

    def extrato(self):
        print(f'{self.titular} Seu saldo é de: R$ {self.__saldo}')

