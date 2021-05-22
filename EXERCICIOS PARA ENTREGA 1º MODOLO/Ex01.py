#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, 
   # divida pelo resultado da divisão inteira e mostre o resultado na tela. 
   # Se não, mostre que a multiplicação não foi maior que 40.
from time import sleep
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
sleep(0.5)
print(f'A) A soma de {n1} + {n2} é = {n1+n2}')
sleep(0.5)
print(f'B) A multiplicação de {n1} x {n2} é = {n1*n2}')
sleep(0.5)
print(f'C) A divisão inteira entre {n1} e {n2} é = {n1//n2}')
sleep(0.5)
if n1 > n2:
    maior = n1
else:
    maior = n2
    print(f'D) O número {maior} é o maior entre os digitados!')
sleep(0.5)
if (n1+n2) % 2 == 0:
    print('E) Resultado da soma é PAR')
else:
    print('E) Resultado da soma é ÍMPAR')
sleep(0.5)
if (n1*n2) > 40:
    div = (n1*n2)/(n1//n2)
    print(f'F) O Resultado da multiplicação {n1}x{n2} é  maior que 40! A divisão de {n1*n2} por {n1//n2} é: {div}')
else:
    print(f'F) A multiplação entre {n1}x{n2} deu menor que 40')
