def Num(numero):
    if numero > 0:
    	return 'P'
    elif numero < 0:
        return 'N'
    elif numero == 0:
        return '0'


numero = float(input('Digite um numero:'))

print(f'{Num(numero)}')