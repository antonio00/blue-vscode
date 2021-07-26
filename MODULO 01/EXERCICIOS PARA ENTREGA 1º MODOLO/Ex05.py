#05 - Refatore o exercício 2, para que uma função receba a frase, 
# faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def tratamento(frase):
    contador = 0
    print(f'Em "{frase}", temos as seguintes vogais: ')
    for letra in frase:
        if letra.lower() in 'aáàâãeéêiíoóôuú': # cada vez que letra rodar em frase vai colocar minuscula lower(), printar
            print(letra, end='')                # vai printar as vogais em letra.
            frase = frase.replace(letra, ' ') # a variavel frase, vai ser alterada para frase sem as vogais
            contador += 1 #vai add quantas vogais aparece,
    print(f'\nA frase sem as vogais fica "{frase}"')
    print(f'{contador} vogais foram retiradas')


frase = input('Digite uma frase: ')
tratamento(frase)