# Escreva um programa que pede a senha ao usuário,
# e só sai do looping quando digitarem corretamente a senha


senha = '5467'
tentativa=input("Digite a senha:")

while senha != tentativa:
    print("Senha Incorreta! Tente novamente!")
    tentativa=input("Digite a senha:")

print("Senha correta. Acesso liberado...")
