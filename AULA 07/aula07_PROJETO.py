def custo_hotel():
    noite = int(input('Quantas noites ficará hospedado: '))
    custoTotal = noite * 140
    print(f'O custo de hospedagem é de: R${custoTotal:.2f}')


def custo_aviao():
    




def custo_carro():
    diaria = 40
    dias = int(input('Quantos dias irá alugar? '))
    desc1 = 50
    desc2 = 20
    total = dias * diaria
    if dias >= 7:
        print(f'Total do aluguel é de: R${(total - desc1)}')
    elif dias >= 3 < 7:
        print(f'Total do aluguel é de: R${(total - desc2)}')
    else:
        print(f'Total do aluguel é de: R${total}')


