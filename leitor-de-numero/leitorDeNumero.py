# criando função
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro! Digite um número valido! \033[m')
        if ok:
            break
    return valor


# Program Principal
numero = leiaInt('Digite um numero: ')
print(f'Você digitou o número {numero}')
