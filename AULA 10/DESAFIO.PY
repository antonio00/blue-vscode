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
print('[1]Candidato A \n[2]Candidato B \n[3]Candidato C \n[4]Candidato D \n[5]Voto Nulo \n[6]Voto em Branco')

candidatoA = 0
candidatoB = 0
candidatoC = 0
candidatoD = 0
nulo = 0
branco = 0
voto = 0

while voto !=7:
    voto = int(input('Digite seu voto: '))
    if voto ==1:
        print('Votou computado no Candidato A')
        