# 8.	Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, 
# o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
from time import sleep
from datetime import datetime
print('==========Calculadora de Aposentadoria==========')
sleep(1)
print('==========Ferramenta desenvolvida por Alunos==========')
sleep(1)
dic= dict()
dic['nome'] = str(input('Nome: '))
nasc= int(input('Ano de nascimento: '))
dic['idade'] = datetime.now().year - nasc
dic['ctps'] = int(input('Digie sua CTPS[0 caso nao possua]: '))
if dic['ctps'] != 0:
    dic['contrato'] = int(input('Ano de Contratação: '))
    dic['salario']= float(input('Salário: R$ '))
    dic['aposenta'] = dic['idade']+((dic['contrato']+35)-datetime.now().year)
print('='*30)
for k,v in dic.items():
    print(f' {k} : {v}')
print()
print('==========Desenvolvido por Alunos da Blue EdTech==========')