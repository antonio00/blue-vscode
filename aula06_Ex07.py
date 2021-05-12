def imprime_menor():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if n1 < n2:
      print(f'{n1} é menor')
    elif n1 > n2:
      print(f'{n2} é menor')
    else:
      print("Os números são iguais.")


imprime_menor()
