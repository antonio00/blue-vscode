def somaImposto():
    taxaImposto = float(input('Qual a taxa de imposto em %: ')) 
    custo = float(input('Qual custo bruto do Produto R$:'))
    realCusto = custo *(taxaImposto/100) + custo
    margemVenda = float(input('Qual Margem de venda em % : '))
    precoVenda = realCusto *(margemVenda/100)
    print(f'Este produto tem: {taxaImposto:.2f}% de imposto ')
    print(f'O custo real é de: R${realCusto:.2f}')
    print(f'O seu preço de venda é: R${precoVenda:.2f}')


somaImposto()

