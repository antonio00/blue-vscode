def trataTexto(texto):
    cont = 0
    for vogal in texto:
        if vogal in 'aáâãeéêiíoõôuú':
            texto = texto.replace(vogal, ' ')
            cont += 1
    print(texto)
    print(f'{cont} vogais retiradas')

texto = str(input('Digite uma frase: ')).lower()
trataTexto(texto)
