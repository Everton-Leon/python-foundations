# criando funções
def aumentar(preco, taxa, formato=False):
    res = preco + (preco * taxa / 100)
    if formato:
        return moeda(res)
    else:
        return res


def diminuir(preco, taxa, formato=False):
    res = preco - (preco * taxa / 100)
    if formato:
        return moeda(res)
    else:
        return res


def dobro(preco, formato=False):
    res = preco * 2
    if formato:
        return moeda(res)
    else:
        return res

def metade(preco, formato=False):
    res = preco / 2
    if formato:
        return moeda(res)
    else:
        return res


def moeda(preco = 0, moeda = 'R$'):
    res = f'{moeda}{preco:.2f}'.replace('.', ',')
    return res


def titulo(msg):
    print('--' * 15)
    print(f'{msg:^25}')
    print('--' * 15)


def resumo(preco, aumento=10, reducao=5):
    titulo("Resumo do Valor")
    print(f'Preço Analizado: \t{moeda(preco)}')
    print(f'Dobro do Preço: \t{dobro(preco, True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redudacao: \t{diminuir(preco, reducao, True)}')
