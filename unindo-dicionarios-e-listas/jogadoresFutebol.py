# inicializando dicionarios e listas
jogador = dict()
gols = list()
geral = list()
while True:

    # coletando dados do usuario
    print('--' * 20)
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    cont = 1
    soma = 0
    while cont <= partidas:
        golsP = int(input(f'Quantos gols na partida {cont}? '))
        gols.append(golsP)
        cont += 1
        soma += golsP

    # inserindo  dados no dicocionario
    jogador['gols'] = gols[:]
    jogador['total'] = soma
    geral.append(jogador.copy())
    gols.clear()

    # verificando erros
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

# interface e respostas
print('-=' * 30)
print(geral)
print('-=' * 30)
print(f'{"Cod":<4} {"nome":<10}  {"gols":<10} {"total":>10}')
print('--' * 20)
for c, v in enumerate(geral):
    print(f'{c:<4} {v["nome"]:<10}  {str(v["gols"]):<10} {v["total"]:>10}')
print('--' * 20)
while True:
    perg = int(input('Mostrar dados de qual Jogador? '))
    if perg == 999:
        break
    while perg > len(geral):
        print(f'\033[1;31mERRO!\033[m Não exite jogador com código {perg} Tente novamente.')
        perg = int(input('Mostrar dados de qual Jogador? (999 para parar) '))
    print(f'-- Levantamento do jogador {geral[perg]["nome"]}: ')
    totp = 1
    for c, v in enumerate(geral):
        if c == perg:
            for i in v['gols']:
                print(f'    No jogo {totp} fez {i} gols.')
                totp += 1
print('<<< VOLTE SEMPRE >>>')
