from random import randint
n = (randint(1, 50), randint(1, 50), randint(1, 50), 
    randint(1, 50), randint(1, 50))

print(f'Números sorteados: {n}')
print(f'O maior número sorteado foi {min(n)}')
print(f'O maior número sorteado foi {max(n)}')
