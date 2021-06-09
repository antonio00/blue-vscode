def soma_limite():
    n1 = float(input('Digite primeiro número: '))
    n2 = float(input('Digite segundo número: '))
    limite = float(input('Qual limite  deseja ultrapassar? '))
    if n1+n2 > limite:
        print('True')
    else:
        print('False')


soma_limite()