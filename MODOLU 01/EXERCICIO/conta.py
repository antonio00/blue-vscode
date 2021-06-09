class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        
    def extrato(self):
        print(f'Seu saldo é {self.saldo}')
    
    def saque(self,valorS):
        if self.saldo >= valorS:
            self.saldo -= valorS
            print(f'Saque de R${valorS} autorizado!')
            print(f'Seu novo saldo é de: R$ {self.saldo}')
        else:
            print(f'Saque R${valorS} não autorizado!')
            print(f'Saldo insunficiente! Saldo disponivel R${self.saldo}')
    
    def deposito(self, valorD):
        self.saldo += valorD

