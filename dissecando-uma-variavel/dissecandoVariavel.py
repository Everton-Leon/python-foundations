# coletando dados do usuario
a = input('Digite algo: ')

# resposta
print(f'O tipo primitivo disso é: {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabetico? {a.isalpha()}')
print(f'É alfanumerico? {a.isalnum()}')
print(f'Esta em maiúsculas? {a.isupper()}')
print(f'Está em minusculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')
