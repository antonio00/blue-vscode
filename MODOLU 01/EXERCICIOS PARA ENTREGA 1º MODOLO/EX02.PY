#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário e 
# conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input('Digite uma frase: ')
print(f'Em "{frase}", temos as seguintes vogais: ')
contador =0 # contar quantas vezes aparece vogal na frase
for letra in frase:
    if letra.lower() in 'aáàâãeéêiíoóôuú': # cada vez que letra rodar em frase vai colocar minuscula lower(), printar
        print(letra, end='')                # vai printar as vogais em letra.
        frase = frase.replace(letra, ' ') # a variavel frase, vai ser alterada para frase sem as vogais
        contador += 1 #vai add quantas vogais aparece,
print(f'\nA frase sem as vogais fica "{frase}"')
print(f'{contador} vogais foram retiradas')

