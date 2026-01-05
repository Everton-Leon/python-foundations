# coletando dados do usuario
c = float(input('Você tem quanto na sua carteira? \033[1;32mR$'))

# convertendo para dolares
d = c/5.17

# resposta
print(f'\033[1;32mR${c:.2f}\033[m convertido em dolar dá \033[1;32mUS{d:.2f}\033[m!')
