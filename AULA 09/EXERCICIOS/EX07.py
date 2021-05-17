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
    print('\nInocente')
elif soma_respostas ==2:
    print('\nSupeito')
elif 3 <= soma_respostas <=4:
    print('\nCumplice')
elif soma_respostas == 5:
    print('\nAssassino')