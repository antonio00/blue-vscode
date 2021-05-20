#02 - Crie um programa que leia a idade e o sexo de várias pessoas.
#  A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#  No final, mostre:
   #  A) quantas pessoas tem mais de 18 anos.
   #  B) quantos homens foram cadastrados.
   #  C) quantas mulheres tem menos de 20 anos.

print('==========BEM VINDO==========')

idade=sexo=homem=mulher=maiorIdade = 0

while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maiorIdade += 1
    
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
    if sexo =='M':
        homem +=1
    if sexo == 'F' and idade < 20:
        mulher += 1
    
    pergunta = (input('Quer Continuar [S/N]'))
    if pergunta in 'Nn':
        break

print('==========RESULTADO==========')
print(f'Total de: {maiorIdade} pessoa(s) acima da maior idade')
print(f'Total de: {homem} homem(ns) cadastrado(s)')
print(f'Tota de: {mulher} mulher(es) com idade inferior a 20 anos')
print()
print('==========Densolvido a base de choro==========')
print()







######## NAO CONSEGUIR VALIDAR ALTERNATIVA C #############
# cadastro = list()
# pessoa = list()
# homem = 0
# MaiorIdade = 0
# Mulher = 0
# while True: 
#     pessoa.append(str(input('Nome:')))
#     pessoa.append(str(input('Sexo: [M/F]')))
#     if pessoa[1] in 'Mm':
#         homem +=1
        
#     if pessoa[1] in 'Ff' and pessoa[2] < 20:
#         Mulher += 1

#     pessoa.append(int(input('Idade:')))
#     if pessoa[2]>= 18:
#         MaiorIdade +=1
#     cadastro.append(pessoa[:])
#     pessoa.clear()
#     pergunta = str(input('Quer Continuar [S/N]'))
#     if pergunta in 'Nn':
#         break
        

# print(f'{homem} cadastro(s) realizado(s)')
# print(f'{MaiorIdade} pessoa(s) maior de idade')
# print(f'Possui {Mulher} menor de idade')


