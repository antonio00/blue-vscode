n= (int(input('Digite o primeiro número:')),
int(input('Digite o segundo número: ')),
int(input('Digite o terceiro número: ')),
int(input('Digite o quarto número: ')))

print(f'Você digitou os valores {n}')
print(f'o número 9 apareceu {n.count(9)}') #conta quantas vezes o 9 na tupla
print(f'O número 3 apareceu na {n.index(3)}ª posição') # mostra a posição do numero 3