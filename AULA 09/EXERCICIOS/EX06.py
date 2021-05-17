paes = int(input("Digite a quantidade de pães: "))
while paes > 50:
    produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))

item = 1
preco_pao = float(input("Qual é o preço do pão? : "))

for c in range(paes):
    print(item, "= R$", round(preco_pao * item, 2))
    item += 1