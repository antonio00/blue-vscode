L = [5, 7, 2, 9, 4, 1, 3]

print(f'A lista original é: {L}') #printa a lista original
print(f'A lista possui {len(L)} posições') # mostra o tamanho da lista
print(f'O maior número é: {max(L)}') #MAX mostra o maior
print(f'O menor número é: {min(L)}') #min mostra o menor
print(f'A soma de todos os valores da lista é {sum(L)}') #cria uma variavel soma com a função 'sum'=soma
L.sort() # ordem crescente
print(f'A ordem crescente é:{L}')# printa a lista em ordem crescente
L.sort(reverse=True) # Ordem decrescente
print(f'A ordem decrescente é:{L}')