def pagamento():
    salarioBase = float(input('Digite Salário do Funcionario: '))
    Horas = float(input('Digite quantidade de horas trabalhada: '))
    valorHora = salarioBase / 40
    adicional = valorHora * 1.5
    Extra = salarioBase + adicional
    if Horas > 40:
        print(f'Salário com Extra é: R${Extra:.2f}')
    else:
        print(f'Salário a receber sem extra: R${salarioBase:.2f}')


pagamento()
