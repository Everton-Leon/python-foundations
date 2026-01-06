# criando função
def ajuda(comando):
    print('\033[43m~' * 27)
    print('  SISTEMA DE AJUDA PyHELP')
    print('~' * 27)
    print('\033[m')
    print('\033[45m~' * (34 + len(comando)))
    print(f'  Acessando o manual do comando {comando}')
    print('~' * (34 + len(comando)))
    print('\033[m')
    print('\033[36;40m')
    print(f'{help(comando)}')
    print('\033[m')


# Programa Principal
c = ''
while True:
    c = str(input('Função ou Biblioteca ->  '))
    if c.upper() == 'FIM':
        break
    else:
        ajuda(c)
