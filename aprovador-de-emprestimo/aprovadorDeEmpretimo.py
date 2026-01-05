# coletando dados do usuario
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos você pretende pagar? '))

# realizando calculos
a = valor / (anos*12)
p = salario*(30/100)

# resposta
print(f'Para pegar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${a:.2f}')
if a > p:
    print(f'Seu imprestimo foi negado!')
else:
    print(f'Obrigado pela preferencia! Em {anos} anos você terá que pagar parcelas de R${a:.2f}')
    
