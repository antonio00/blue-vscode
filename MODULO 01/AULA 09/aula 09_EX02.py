# Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa
# sobre um crime. As perguntas são:
# ○ “Telefonou para a vítima?”
# ○ “Esteve no local do crime?”
# ○ “Mora perto da vítima?”
# ○ “Devia para a vítima?”
# ○ “Já trabalhou com a vítima?”
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
# “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino”. Caso contrário, ele
# será classificado como “Inocente”.


respostas = []
respostas.append(input('Telefonou para a vítima? 1/Sim ou 0/Não: '))
respostas.append(input('Esteve no local do crime? 1/Sim ou 0/Não: '))
respostas.append(input('Mora perto da vítima? 1/Sim ou 0/Não: '))
respostas.append(input('Devia para a vítima? 1/Sim ou 0/Não: '))
respostas.append(input('Já trabalhou com a vítima? 1/Sim ou 0/Não: '))

soma_respostas = 0
for i in respostas:
  soma_respostas += int(i)
if soma_respostas <2:
    print('\nVocê é Inocente')
elif soma_respostas ==2:
    print('\nVocê é Supeito')
elif 3 <= soma_respostas <=4:
    print('\nVocê é Cumplice')
elif soma_respostas == 5:
    print('\nVocê é Assassino')