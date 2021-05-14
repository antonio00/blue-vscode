##REMOVE NAO FUNCIONA PARA STRING
# palavra = 'String'

# if 'i' in palavra:
#     palavra.remove('i')
#     print (palavra)
# else:
#     print('O valor i, não existe na lista!')


####### PARA STRING DEVE UTILIZAR REPLACE
# palavra = 'String'

# if 'i' in palavra:
#    print(f'Eu achei o i na {palavra}')
#    novaPalavra = palavra.replace('i', '1')
#    print (f'A palavra sem o i é {novaPalavra}')
# else:
#     print('O valor i, não existe na lista!')


####--- MOSTRA A POSICAO E O VALOR NELE----#####
# lista=[1,2,3,4,5,6]

# for p, c in enumerate(lista): ###P= POSICAO; C= VALOR
#     print(f'Na posição {p} está o valor {c}')
######################################################

#  lista=[1,2,3,4,5,6]

# for c in enumerate(lista): ###P= POSICAO; C= VALOR
#     print(c, end=' ') # end serve para mostrar os valores na mesma linha

######################################################
# lista=[4, 6, 2, 9, 1, 6]
# print(lista)# printa a lista em ordem original
# lista.sort() # ordem crescente
# print(lista)# printa a lista em ordem crescente
# lista.sort(reverse=True) # Ordem decrescente
# print (lista) # printa a lista em ordem decrescente

# print(len(lista)) # mostra o tamanho da lista, conta os valores.
# ##########################################################

########LIGAÇÃO DE LISTAS ########
# A = [0,1,2,3,4,5]
# B = A

# B[2]=7

# print(f'Lista A: {A}')
# print(f'Lista B: {B}')

############################################
# COPIA DE LISTA #
# a = [0,1,2,3,4,5]
# b = a[:]

# b[2]=7

# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
############################################



