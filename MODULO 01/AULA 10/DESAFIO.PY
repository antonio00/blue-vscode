# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 

# Os códigos utilizados são:
# 1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;

print('Escolha um número para votar:')
print('[1]Candidato A \n[2]Candidato B \n[3]Candidato C \n[4]Candidato D \n[5]Voto Nulo \n[6]Voto em Branco \n[7] Encerrar/Sair')

candidatoA = 0
candidatoB = 0
candidatoC = 0
candidatoD = 0
nulo = 0
branco = 0
voto = 0

while voto !=7: #Enquanto voto for diferente de 7, faça:

    voto = int(input('Digite seu voto: '))
    if voto ==1:
        print('Votou computado no Candidato A')
        candidatoA += 1
    elif voto ==2:
        print('Votou computado no Candidato B')
        candidatoB += 1
    elif voto ==3:
        print('Votou computado no Candidato C')
        candidatoC += 1
    elif voto ==4:
        print('Votou computado no Candidato 4')
        candidatoD += 1
    elif voto ==5:
        print('Votou NULO')
        nulo += 1
    elif voto ==6:
        print('Votou em BRANCO')
        branco += 1

print('='*30)
print('VOTAÇÃO ENCERRADA')
print('='*30)
print(f'Candidato A teve: {candidatoA} votos!')
print(f'Candidato B teve: {candidatoB} votos!')
print(f'Candidato C teve: {candidatoC} votos!')
print(f'Candidato D teve: {candidatoD} votos!')
print(f'Houve {nulo} votos NULOS!')
print(f'Houve {branco} votos em Branco!')
        