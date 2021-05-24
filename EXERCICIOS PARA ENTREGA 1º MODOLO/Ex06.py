#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".


from time import sleep
print('='*50)
print('DESENVOLVIDO POR ALUNOS DA BLUE EDTECH')
print('='*50)
respostas = [] # criar lista vazia
respostas.append(int(input('Telefonou para a vítima? 1/Sim ou 0/Não: '))) #append - adcionar na lista o valor digitado
respostas.append(int(input('Esteve no local do crime? 1/Sim ou 0/Não: ')))
respostas.append(int(input('Mora perto da vítima? 1/Sim ou 0/Não: ')))
respostas.append(int(input('Devia para a vítima? 1/Sim ou 0/Não: ')))
respostas.append(int(input('Já trabalhou com a vítima? 1/Sim ou 0/Não: ')))


soma_respostas = 0
for i in respostas:
  soma_respostas += int(i)
if soma_respostas <2:
    sleep(1)
    print('\nVocê está liberado, provamos sua inocência')
elif soma_respostas ==2:
    sleep(1)
    print('\nPedimos que não sai da cidade você ainda é um supeito')
elif 3 <= soma_respostas <=4:
    sleep(1)
    print('\nVocê será indiciado como cumplice no assassinato')
elif soma_respostas == 5:
    sleep(1)
    print('======POLICIAL PRENDA ESTE INDIVIDUO=====')
    print('\nVocê é o Assassino')

print('='*80)
print('Este caso foi encerrado sob supervisão de Thi.Code e Viniolegon')
print('='*80)