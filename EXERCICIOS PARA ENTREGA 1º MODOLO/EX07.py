#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]] # cria uma lista e dentro duas listas vazias
num = 0 # variavel inicia zerado, e recebe valor digitado em input

for c in range(1,8): # usei 1 a 8 para poder formartar o texto do input no for
    num = int(input(f'Digite o {c}º número: ')) #valor digitado vai para variavel num
    if num % 2 ==0:
        lista[0].append(num) # todo numero divisivel por 2 vai para o indice 0[pares] da lista principal, dentro outra lista
    else:
        lista[1].append(num) # os que a dividao por 2 nao for exata, vao para indice 1[impar] da lista princ, dentro da lista

lista[0].sort() # ordeno de forma crescente todos os valores digitados dentro do indice 0, que tbm é lista
lista[1].sort() # ordeno de forma crescente todos os valores digitados dentro do indice 1, que tbm é lista
print(f'O numeros pares foram: {lista[0]}')
print(f'O numeros pares foram: {lista[1]}')
