# 3.	Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#  No final, mostre o conteúdo sa estrutura na tela. A média para aprovação é 7. 
# Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.


aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] =  float(input(f'Média de {aluno["nome"]}:'))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] <7:
    aluno['situacao'] = 'Recurepação'
else:
    aluno['situcao'] = 'FERROU! REPROVADO'
    print()
for k, v in aluno.items():
    print(f'{k}: {v}')
