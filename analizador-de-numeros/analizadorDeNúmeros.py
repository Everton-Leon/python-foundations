# criando lista
valores = []

# enchendo a lista
for c, v in enumerate(range(0,5)):
    valores.append(int(input(f'Digite um número na posição {c}: ')))
print(f'A lista ficou assim: {valores}')

# pegando o maior e o menor valor da lista
maior = max(valores)
menor = min(valores)

# resposta
print(f'O maior valor digitado foi {maior} e está na posição ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end='')
print(f'\nO menor valor digitado foi {menor} e está na posição ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end='')
