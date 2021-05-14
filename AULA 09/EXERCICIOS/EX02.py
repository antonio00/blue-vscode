# for c in range(0,11,1):
#     print(c)

# for c in range(10,0, -1):
#     print(c)
lista=list(range(11)) #converte um range em list
print(f'A lista em ordem crescente é:{lista}') 
lista.sort(reverse=True) #ordena lista em decrescente
print(f'A lista em ordem decrescente é:{lista}') 
