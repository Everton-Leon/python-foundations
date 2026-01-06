# inicializando variaveis
somai = 0
cont = 0
maioridadehomem = 0
nomevelho = ''

# coletando dados do usuario
for i in range(1, 5):
    print(f'----- {i}° PESSOA -----')
    nome = str(input(f'Nome: ')).strip().upper()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo(M ou F): ')).strip().upper()

    # calculos
    somai += idade
    if sexo == 'F' and idade < 20:
        cont += 1
    if i == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and maioridadehomem < idade:
        maioridadehomem = idade
        nomevelho = nome
media = somai / 4

# reposta
print(f'A média da idade do grupo é {media}')
print(f'{cont} mulheres tem menos de 20 anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')

