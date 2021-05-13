def ficha(jogador='[Nao informado]', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s).')


jog = str(input('Nome do jogador: '))
gols = str(input('Gols marcados: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0 
if jog.strip()== '':
    ficha(gol=gols)
else:
    ficha(jog, gols)

