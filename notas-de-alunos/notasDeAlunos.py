# criando listas
geral = list()
aluno = list()
notas = list()
while True:

    # coletando dados e inserindo na lista
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(notas[:])
    aluno.append(media)
    geral.append(aluno[:])
    aluno.clear()
    notas.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(geral)

# interface
print('-=' * 30)
print(f'{"No.":<5}{"NOME":<12} {"MÉDIA":>7}')
print('--' * 15)

# resposta
for c, v in enumerate(geral):
    print(f'{c:<3}  {v[0]:<10} {v[2]:>9}')
print('--' * 15)
while True:
    dados = int(input('Mostrar dados de qual aluno? (999 interrompe) '))
    for c, v in enumerate(geral):
        if c == dados:
            print(f'Notas de {v[0]} são {v[1]}')
    if dados == 999:
        break
print('Finalizando...')
print('<<< Volte Sempre >>>')
