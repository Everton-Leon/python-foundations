# coletando dados do usuario
p = float(input('Qual o preço do produto? R$'))

# calculando desconto
l = p-(p*(5/100))

# resposta
print(f'O produto que custava R${p}, na promoção com 5% de desconto vai custar R${l:.2f}')
