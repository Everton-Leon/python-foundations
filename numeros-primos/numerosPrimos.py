# coletando dados do usuario
n = int(input('Digite um número: '))

# realizando calculos
tot = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\033[36m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(i, end = ' ')

# resposta
print(f'\n\033[mO número {n} foi divisivel {tot} vezes')
if tot == 2:
    print(f'{n} é um número primo!')
else:
    print('E por isso ele não é um número primo')

