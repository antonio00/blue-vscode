class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def comer(self):
        print(f'A pessoa {self.nome} está comendo...')
        
    def falar(self, texto):
        print(f'A pessoa {self.nome}, está falando: {texto}')

    def mostraDados(self):
        print(f'O nome é: {self.nome}')
        print(f'A idade é: {self.idade}')
        print(f'O sexo é: {self.sexo}')