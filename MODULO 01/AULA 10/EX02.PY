#02 - Faça um programa que leia o sexo biológico de uma pessoa, 
# mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = input('Digite seu sexo [M/F]: ').strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Você não digitou M ou F')
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()
print(f'Sexo {sexo} registrado.')