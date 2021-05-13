# def soma(n1=0, n2=0, n3=0, n4=0):
#     soma = n1 + n2 + n3 + n4
#     print(f'A soma é: {soma}')


# soma(10, 30)
# soma(4, 7, 5)
# soma(3, 2, 6, 8) """


# """ n1 = 10
# n2 = 30
# soma = n1 + n2
# print(f'A soma é: {soma}')

# n1 = 4
# n2 = 7
# soma = n1 + n2
# print(f'A soma é: {soma}')

# n1 = 2
# n2 = 3
# soma = n1 + n2
# print(f'A soma é: {soma}')


# ESCOPO = ESPAÇO
# def area(larg, comp):
#     """
#     -> Funcao area:
#     Recebe dois parametros,
#     Um para a largura(larg)
#     Outro para comprimento(comp)
#     sem retorno
#     criado pelo @toim_leite

#     """
#     areaVar = larg * comp #Variavel de escopo local
#     print(f'A área de um terreno {larg} x {comp} é de {areaVar}m²')


# areaVar = 0 #variavel escopo global
# l = float(input('Largura(m): '))
# c = float(input('Comprimento (m): '))

# print(areaVar)

def soma(a=0, b=0, c=0):
    s= a + b + c
    return s

def media(x,y,z):
    som = soma(x,y,z)
    media = som /3
    return media


n1= float(input('N1: '))
n2= float(input('N2: '))
n3= float(input('N3: '))

print(f'A media é: {media(n1,n2,n3):.2f}')
