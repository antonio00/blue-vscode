idade = sexo = contadorHomens = contadorIdade = contadorMulheres =  0

while True:
    idade = int(input('Digite sua idade por favor: '))
    if idade > 18:
        contadorIdade += 1

    sexo = input('Certo... Agora me informe seu sexo biológico: ').strip().upper()[0]
    if sexo == "M":
        contadorHomens += 1
    if sexo == "F" and idade < 20:
        contadorMulheres += 1

    continuar = input('\nDeseja continuar cadastrando? [S/N]: \n').strip().upper()[0]
    if continuar == "N":
        break  

print(f"\nForam cadastrados {contadorHomens} homens.\n{contadorIdade} pessoas tem mais de 18 anos.\n{contadorMulheres} mulheres tem menos de 20 anos.")