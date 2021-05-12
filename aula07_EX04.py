def voto():
    from datetime import date
    atual = date.today().year
    ano = int(input('Em que ano você nasceu? '))
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade}: VOTO OBIGATÓRIO.')


voto()