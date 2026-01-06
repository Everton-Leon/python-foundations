# inicializando variaveis
maisdeMil = maisBarato = nomeMaisBarato = cont = total = 0

while True:
    # interface
    print('-=-' * 10)
    print('LOJA DO EVERTON'.center(30))
    print('-=-' * 10)

    # coletando dados
    nome = str(input('Digite o nome do produto: '))
    preço = int(input('Digite o preço do produto: R$'))
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while op not in 'SsNn':
        op = str(input('Quer continuar? [S/N] '))
    total += preço
    cont += 1
    # coletando informações
    if cont == 1:
        maisBarato = preço
        nomeMaisBarato = nome
    else:
        if preço < maisBarato:
            maisBarato = preço
            nomeMaisBarato = nome
    if preço >= 1000:
        maisdeMil += 1
    if op in 'Nn':
        break

# resposta
print(f'O preço total dos produtos foi R${total:.2f}')
print(f'{maisdeMil} produtos custam mais de mil rais.')
print(f'O produto mais barato é {nomeMaisBarato} e custa R${maisBarato:.2f} ')
